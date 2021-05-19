import json

f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
responses = json.load(f)
files = []
file_names = ["large 1:\n", "medium 1:\n", "medium 2:\n", "medium 3:\n", "small 1:\n", "small 2:\n", "small 3:\n", "small 4:\n", "small 5:\n", "small 6:\n", "small 7:\n"]
files.append(open('D:\github\Dissertation\data\\treated\large 1.txt', 'r', errors='ignore'))
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


write = open('D:\github\Dissertation\data\Results\Bing API.txt', 'w')
index = 0
for file in files:
    lines = file.readlines()
    write.write(file_names[index])
    result = []
    for line in lines:
        line = line.strip('\n')
        test = line.split(" ")
        if test[0] in responses:
            corrections = responses[test[0]]
            found = 0
            for corr in corrections:
                if test[1] == corr["suggestion"]:
                    result.append(corr["suggestion"] + " " + test[1] + "\n")
                    found = 1
                    break
            if found == 0:
                result.append(line + "\n")
        else:
            result.append(line + "\n")

    write.writelines(result)
    write.flush()
    index += 1

