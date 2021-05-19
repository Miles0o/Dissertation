import json

f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
responses = json.load(f)
files = []
file_names = ["large 1:", "medium 1:", "medium 2:", "medium 3:", "small 1:", "small 2:", "small 3:", "small 4:", "small 5:", "small 6:", "small 7:"]
files.append(open('D:\github\Dissertation\data\\treated\large 1.txt.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\medium 1.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\medium 2.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\medium 3.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 1.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 2.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 3.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 4.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 5.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 6.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 7.txt', 'r', errors='ignore'))

index = 0
for file in files:
    lines = file.readlines()
    write = open('data/Results/Bing API.txt', 'w')
    write.write(file_names[index])
    result = []
    for line in lines:




    write.writelines(result)
    index += 1