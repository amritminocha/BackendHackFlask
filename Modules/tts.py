import os
import requests
import uuid

ELEVENLABS_API_KEY = "19dfe9f4f3ac5d8158e25685510fdc95"

all_voices=[]
stability= 0.50
similarity = 0.75

#gets list of voices
def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()["voices"]
print()

all_voices = get_voices()

def generate_audio(text, output_path,voice_name):
    voices = all_voices

    if not voices:
        print("No voices found")
        return
    
    try:
        voice_id = next(filter(lambda v: v["name"] == voice_name, voices))["voice_id"]
    except StopIteration:
        voice_id = voices[0]["voice_id"]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "content-type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity,
        },
        "model_id": "eleven_multilingual_v2"
    }
    response = requests.post(url, json=data, headers=headers)
    
    # Generate a unique filename using uuid
    unique_filename = f"{uuid.uuid4()}.mp3"
    full_output_path = os.path.join(output_path, unique_filename)

    #Write to file
    with open(full_output_path, "wb") as output:
        output.write(response.content)

    return full_output_path