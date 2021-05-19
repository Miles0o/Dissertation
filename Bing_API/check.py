import json

f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
check = open('D:\github\Dissertation\data\\treated\small 6.txt', 'r', errors='ignore')

lines = check.readlines()
responses = json.load(f)

print(len(responses))

for line in lines:
    if line.split(" ")[0] not in responses:
        print(line.split(" ")[0])

