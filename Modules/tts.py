import os
import requests
import uuid

ELEVENLABS_API_KEY = "19dfe9f4f3ac5d8158e25685510fdc95"

#gets list of voices
def get_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()["voices"]


