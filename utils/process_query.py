from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import warnings
import os
from dotenv import load_dotenv, dotenv_values

warnings.filterwarnings("ignore")
load_dotenv()

key = os.getenv("Gemini_API_key")
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True,
                               google_api_key=key, temperature=1.0)


def query_processer(query_source):
    user_query = query_source
    response = model(
        [
            SystemMessage(
                content=f"""You are a virtual desktop assistant and your name is "Luna" and you are developed by 
                "Hamdan" you can perform many tasks like Opening websites, playing song," "telling time, 
                answering your questions, performing YouTube search, etc. But all these tasks are personal tasks. not 
                only these tasks but you are able to perform local tasks on user's computer, but You are currently 
                under development so you can mistake and you can deliver stupid answers and behavior. Now answer this 
                question and if this question asks about you then introduce your self as "Luna and if not then simpy 
                answer this question"""
            ),
            HumanMessage(content=user_query),
        ]
    )

    return response.content
