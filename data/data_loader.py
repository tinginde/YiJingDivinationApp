import json

def  load_interpretations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_interpretation(hexagram_name, interpretations):
    return interpretations.get(hexagram_name, "未找到此卦象的解释。")