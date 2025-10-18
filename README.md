# 易經卦象解釋小工具 🧧

這是一個使用 [Streamlit](https://streamlit.io/) 開發、並部署在 [Zeabur](https://zeabur.com/) 平台上的簡易應用。使用者輸入問題後，
系統將根據隨機卦象，結合 AI 生成對應的卦象解釋，提供人生方向上的參考。

## 🌐 線上體驗：
👉 https://streamlit-yijing.zeabur.app/

## 主要功能

- 以擲銅錢方式隨機產生六爻並組成卦象
- 顯示卦名並從資料庫中取得對應的解釋
- 使用 OpenAI API 依據使用者問題與卦象結果給出占卜建議
- 紀錄並顯示累計訪問人數

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

---

# Yi Jing Hexagram Divination Helper 🧧

This is a lightweight application built with [Streamlit](https://streamlit.io/) and deployed on the [Zeabur](https://zeabur.com/) platform. After a user submits a question, the system randomly generates a hexagram and combines it with AI-generated interpretations to offer guidance for life decisions.

## 🌐 Live Demo
👉 https://streamlit-yijing.zeabur.app/

## Key Features

- Randomly generate six lines using the coin-toss method to form a hexagram
- Display the hexagram name and retrieve the corresponding interpretation from the dataset
- Use the OpenAI API to provide divination suggestions based on the user's question and the hexagram result
- Track and display the total number of visits

## Installation

1. Install dependencies after cloning the repository:

   ```bash
   pip install -r requirements.txt
   ```

2. Prepare an OpenAI API key and set it either as the `OPENAI_API_KEY` environment variable or in Streamlit `secrets`.

## Running Locally

Run the following command from the project root:

```bash
streamlit run app.py
```

Open your browser to access the interface. Enter your question and click **"開始占卜 / Start Divination"** to receive the result.

## Project Structure

- `app.py`: Main application containing the UI and core logic
- `data/`: Hexagram data and helper functions for loading it
- `utils/`: Helper functions for interacting with the OpenAI API
- `requirements.txt`: List of required Python packages

Feel free to modify and extend this project.
