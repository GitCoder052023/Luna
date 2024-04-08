import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()


def query_processer(query_source):
    messages = []

    while True:
        query = query_source

        genai.configure(api_key=os.getenv("Gemini_API_key"))

        model = genai.GenerativeModel('gemini-pro')
        print("Generating content for you...")

        message = query
        messages.append({
            "role": "user",
            "parts": [message],
        })

        response = model.generate_content(messages)

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        return response.text


def write_mail(topic):
    genai.configure(api_key=os.getenv("Gemini_API_key"))
    model = genai.GenerativeModel('gemini-pro')
    Input = topic

    response = model.generate_content(Input)
    return response.text
