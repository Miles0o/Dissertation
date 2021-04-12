from typing import Dict

import requests
import json

class API_talker:

    def __init__(self):
        # innitilisation
        api_key = "e5374b4ddc834dbbb0b9b019cd490504"
        self.endpoint = "https://api.bing.microsoft.com/v7.0/spellcheck"
        self.params = {'mkt': 'en-GB', 'mode': 'proof'}
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Ocp-Apim-Subscription-Key': api_key
        }

    def API_call(self, words):
        data = {'text': words}
        response = requests.post(self.endpoint, headers=self.headers, params=self.params, data=data)
        json_response = response.json()
        #send, recive, return
        return json.dumps(json_response, indent=4)

    def API_callPre(self, words, precontext):
        self.params['preContextText'] = precontext
        return self.API_call(words)


    def API_callPrePost(self, words, precontext, postcontext):
        API_talker.params['preContextText'] = precontext
        API_talker.params['postContextText'] = postcontext
        return self.API_call(words)
