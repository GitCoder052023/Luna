import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def Activate_LunaTXT():
    genai.configure(api_key=os.getenv("Gemini_API_key"))
    model = genai.GenerativeModel('gemini-pro')
    messages = []

    while True:
        user_input = input("You: ")
        messages.append({
            "role": "user",
            "parts": [user_input],
        })

        response = model.generate_content(messages)

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        print("Luna:", response.text)
