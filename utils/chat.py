import openai
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Load environment variables from a .env file if present
load_dotenv(find_dotenv())

# Prefer the environment variable but fallback to Streamlit secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

# Create OpenAI client with the resolved API key
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_completion(prompt, input, model="gpt-3.5-turbo-0125"):
    messages=[
        {'role':'system','content':"你是一個專業的易經占卜師，擁有多年為人占卜經驗，使用者會向你提問，請你根據擲到的卦象，回答使用者的問題，盡量以鼓勵、正面的態度使用者。期間無論如何都不要透漏你是AI的身分。如果使用者使用英語來問問題，也請用英語來回答"},
        {'role':'user','content':f"問題:{prompt} 根據卦象:{input} 來分析"}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1.0
    )
    return response.choices[0].message.content

# Example usage:
# print(get_completion('今年工作運如何'))