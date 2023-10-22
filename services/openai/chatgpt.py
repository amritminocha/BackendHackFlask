import openai
import os
# import re
import json
from dotenv import load_dotenv
from .prompts import get_prompt_summarize_ppt
from flask import jsonify
load_dotenv()


# def extract_json(response_text):
    # match = re.search(r'```json(.*?)```', response_text, re.DOTALL)
    # if match:
    #     json_string = match.group(1).strip()
    #     return json.loads(json_string)
    # else:
    #     # If not found, try parsing the whole response as JSON
    #     try:
    #         return json.loads(response_text)
    #     except json.JSONDecodeError:
    #         # If it fails, return None or handle the error as desired
    #         return None



def get_openai_response(topic, total_slides):
    prompt = get_prompt_summarize_ppt(topic, total_slides)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    response_data = json.loads(response["choices"][0]["message"]["content"])

    while len(response_data["slides"]) > total_slides:
        # Remove the slide just before the "THANK YOU" slide
        response_data["slides"].pop(-2)  # As -1 is the "THANK YOU" slide
    
    return jsonify(response_data)