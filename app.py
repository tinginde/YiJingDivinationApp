import streamlit as st
import random
from data.data_loader import load_interpretations, get_interpretation
from utils.chat import get_completion

ba_gua_numbers_reverse={
    999: '乾卦',
    666: '坤卦',
    966: '震卦',
    696: '巽卦',
    969: '坎卦',
    996: '離卦',
    669: '艮卦',
    699: '兌卦'
}

liusi_gua_ch = {
    "乾上乾下": "乾卦",
    "坤上坤下": "坤卦",
    "坎上震下": "屯卦",
    "艮上坎下": "蒙卦",
    "坎上乾下": "需卦",
    "乾上坎下": "訟卦",
    "坤上坎下": "師卦",
    "坎上坤下": "比卦",
    "巽上乾下": "小畜卦",
    "乾上兌下": "履卦",
    "坤上乾下": "泰卦",
    "乾上坤下": "否卦",
    "離上乾下": "同人卦",
    "乾上離下": "大有卦",
    "坤上艮下": "謙卦",
    "震上坤下": "豫卦",
    "坤上震下": "隨卦",
    "艮上巽下": "蠱卦",
    "坤上兌下": "臨卦",
    "巽上坤下": "觀卦",
    "離上震下": "噬嗑卦",
    "艮上離下": "賁卦",
    "艮上坤下": "剝卦",
    "坤上艮下": "復卦",
    "乾上震下": "無妄卦",
    "艮上乾下": "大畜卦",
    "震上艮下": "頤卦",
    "巽上離下": "大過卦",
    "坎上坎下": "坎卦",
    "離上離下": "離卦",
    "兌上艮下": "咸卦",
    "艮上震下": "恆卦",
    "乾上艮下": "遯卦",
    "震上乾下": "大壯卦",
    "離上坤下": "晉卦",
    "坤上離下": "明夷卦",
    "巽上離下": "家人卦",
    "離上兌下": "睽卦",
    "坎上艮下": "蹇卦",
    "艮上坎下": "解卦",
    "艮上坤下": "損卦",
    "震上巽下": "益卦",
    "兌上乾下": "夬卦",
    "乾上巽下": "姤卦",
    "兌上坤下": "萃卦",
    "坤上巽下": "升卦",
    "澤上坎下": "困卦",
    "坎上兌下": "井卦",
    "澤上離下": "革卦",
    "離上風下": "鼎卦",
    "震上震下": "震卦",
    "艮上艮下": "艮卦",
    "巽上艮下": "漸卦",
    "兌上震下": "歸妹卦",
    "離上震下": "豐卦",
    "離上艮下": "旅卦",
    "巽上巽下": "巽卦",
    "兌上兌下": "兌卦",
    "巽上坎下": "渙卦",
    "坎上兌下": "節卦",
    "兌上風下": "中孚卦",
    "艮上震下": "小過卦",
    "坎上離下": "既濟卦",
    "離上坎下": "未濟卦",
    "震上坎下":"解卦",
    "震上離下":"豐卦",
    "震上震下":"雷卦",
    "震上兌下":"歸妹卦",
    "巽上震下":"益卦",
    "巽上兌下":"中孚卦",
    "坎上巽下":"井卦",
    "離上巽下":"鼎卦",
    "兌上巽下":"大過卦",
    "兌上坎下":"困卦",
    "兌上離下":"革卦",
    "艮上兌下":"損卦"
}
# 加载卦象解释
interpretations = load_interpretations('./data/sixtyfour_gua_meaning.json')

# 擲銅錢函數
def toss_coin():
    return random.choice([6,9])

# 初始化session_state
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''
if 'clear_flag' not in st.session_state:
    st.session_state.clear_flag = False

def clear_input():
    # 设置标志位为True，触发清除操作
    st.session_state.clear_flag = True

# 主應用函數
def main():
    st.title('易經占卜')
    st.subheader('探索易經的奧秘')
    st.write("""
歡迎來到易經占卜網站，這裡您可以通過古老的易經卦象來探索生活中的各種可能性。
無論是關於個人發展、職業選擇，還是人際關係的問題，易經占卜都能為您提供獨特的洞察和指引。
""")
    # 检查是否需要清除输入
    if st.session_state.clear_flag:
        # 清除输入并重置标志位
        st.session_state["user_input"] = ''
        st.session_state["clear_flag"] = False
        
    # value输入控件的初始值, key唯一的标识符（ID）,on_changeon_change指定当输入控件的值发生变化时，应该调用的函数
    user_question = st.text_input('請輸入你的問題：', value=st.session_state.user_input, key='user_input', on_change=reset_clear_flag)
    
    # 创建一个文本输入框，并使用session_state变量来存储输入值
    col1, col2 = st.columns(2)
    with col1:
        if st.button('開始占卜'):
            # 占卜邏輯
            hexagram_numbers = [toss_coin() for _ in range(6)]
            hexagram_numbers.reverse()
            hexagram_key = ''.join(map(str, hexagram_numbers))
            up_gua = ba_gua_numbers_reverse.get(int(hexagram_key[:3]))
            down_gua = ba_gua_numbers_reverse.get(int(hexagram_key[3:]))
            hexagram_name = liusi_gua_ch.get(up_gua[0]+"上" + down_gua[0] + "下", None)
            interpretation = get_interpretation(hexagram_name, interpretations)
            final_interpretation = get_completion(user_question, interpretation)
            # st.session_state['query_result'] = f'您的卦象是：{hexagram_name}\n卦象解释：{final_interpretation}'
            st.write('您的卦象是：', hexagram_name)
            st.write('卦象解釋', final_interpretation)

    with col2:
        st.button('清除輸入', on_click=clear_input)    

        
# 如果文本输入框的值被修改，重置清除标志位
def reset_clear_flag():
    st.session_state.clear_flag = False

# 啟動應用
if __name__ == '__main__':
    main()
