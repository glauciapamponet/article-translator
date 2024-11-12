import json
import requests
import os

SUBS_KEY = "SUBSCRIPTION KEY HERE"
ENDPOINT_TRANSLATOR = "https://api.cognitive.microsofttranslator.com/"
API_VERSION = "3.0"
LOCATION = "eastus2"
FROM_LANGUAGE = 'en'
TARGET_LANGUAGE = "pt-br"


def translator_text(text):
    path = '/translate'
    url = ENDPOINT_TRANSLATOR + path
    headers = {
        'Ocp-Apim-Subscription-Key': SUBS_KEY,
        'Ocp-Apim-Subscription-Region': LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }

    body = [{'text': text}]
    params = {
        'api-version': API_VERSION,
        'from': FROM_LANGUAGE,
        'to': TARGET_LANGUAGE
    }

    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']