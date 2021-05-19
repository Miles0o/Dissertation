from Bing_API import API_talker
import json
import time

read = open('D:\github\Dissertation\data\\treated\small 6.txt', 'r', errors='ignore')
API = API_talker.API_talker()
f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
responses = json.load(f)
lines = read.readlines()
for line in lines:
    time.sleep(0.4)
    response = API.API_call(line.split(" ")[0])
    new = json.loads(response)
    try:
        if new['flaggedTokens'][0]['token'] not in responses:
            responses[new['flaggedTokens'][0]['token']] = new['flaggedTokens'][0]['suggestions']
    except:
        print(new)
with open('D:\github\Dissertation\Bing_API\Bing_response.json', 'w') as fp:
    json.dump(responses, fp)