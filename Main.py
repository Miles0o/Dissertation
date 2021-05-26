import Shell_Bing as Shell

write = open('D:\github\Dissertation\data\Results\Bing API\System pass 3.txt', 'a')
files = []
file_names = ["large 1:\n", "medium 1:\n", "medium 2:\n", "medium 3:\n", "small 1:\n", "small 2:\n", "small 3:\n", "small 4:\n", "small 5:\n", "small 6:\n", "small 7:\n"]
#files.append(open('D:\github\Dissertation\data\\treated\large 1.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\medium 1.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\medium 2.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\medium 3.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 1.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 2.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 3.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 4.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 5.txt', 'r', errors='ignore'))
#files.append(open('D:\github\Dissertation\data\\treated\small 6.txt', 'r', errors='ignore'))
files.append(open('D:\github\Dissertation\data\\treated\small 7.txt', 'r', errors='ignore'))

spellchecker = Shell.shell()
index = 10
for file in files:
    lines = file.readlines()
    write.write(file_names[index])
    result = []
    for line in lines:
        line = line.strip('\n')
        test = line.split(" ")
        correction = spellchecker.lookup(test[0], test[1])
        result.append(correction + " " + test[1] + "\n")

    write.writelines(result)
    write.flush()
    index += 1