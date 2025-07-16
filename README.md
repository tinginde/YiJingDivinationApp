# 易經占卜應用

這是一個使用 [Streamlit](https://streamlit.io/) 打造的簡易易經占卜網站，可以透過擲銅錢產生卦象，並運用 OpenAI 的聊天模型對卦象進行解讀，提供使用者參考。

## 主要功能

- 以擲銅錢方式隨機產生六爻並組成卦象
- 顯示卦名並從資料庫中取得對應的解釋
- 使用 OpenAI API 依據使用者問題與卦象結果給出占卜建議

## 安裝

1. 取得程式碼後，請先安裝依賴套件：

   ```bash
   pip install -r requirements.txt
   ```

2. 準備 OpenAI API 金鑰，並以環境變數 `OPENAI_API_KEY` 或在 Streamlit `secrets` 中設定。

## 執行方式

在專案根目錄下執行：

```bash
streamlit run app.py
```

開啟瀏覽器即可看到應用介面，輸入您的問題點擊「開始占卜」即可得到結果。

## 專案結構

- `app.py`：應用主程式，包含使用者介面與主要邏輯
- `data/`：存放卦象資料與讀取函式
- `utils/`：與 OpenAI API 溝通的輔助函式
- `requirements.txt`：所需 Python 套件列表

歡迎自由修改與擴充此專案。

