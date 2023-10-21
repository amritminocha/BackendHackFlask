import openai
import os
from dotenv import load_dotenv
load_dotenv()

def get_openai_response():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Give me an introduction about chatGPT"},
        ]
    )
    return response["choices"][0]["message"]["content"]