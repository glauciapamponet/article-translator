import requests
import os

SUBS_KEY = ""
ENDPOINT_TRANSLATOR = ""
LOCATION = "eastus2"
FROM_LANGUAGE = 'en'
TARGET_LANGUAGE = "pt-br"


def translator_text(text):
    path = '/translate'
    url = ENDPOINT_TRANSLATOR + path
    headers = {
        'Ocp-Apim-Subscription-Key': SUBS_KEY,
        'Ocp-Apim-Subcription-Region': LOCATION,
        'Content-Type': 'application/json',
        'X-ClienttraceId': str(os.urandom(16))
    }

    body = [{'text': text}]
    params = {
        'api-version': '',
        'from': FROM_LANGUAGE,
        'to': TARGET_LANGUAGE
    }

    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]["translations"][0]["text"]
