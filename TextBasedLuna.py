import google.generativeai as genai
from dicts import key

def Activate_KiaraTLDR():
    genai.configure(api_key=key)
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
