# treats test data
read = open('D:\github\Dissertation\data\data\medium 3.txt', 'r', errors='ignore')
write = open('D:\github\Dissertation\data\\treated\medium 3.txt', 'a')
open = open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r', errors='ignore')
punctuations = '''!+=()-[]{};:'"\,<>./?@#$%^&*_~1234567890\n'''

lines = open.readlines()
dic = []
for line in lines:
    dic.append(line.split(" ")[0])

lines = read.readlines()
count = 0
list = []
for line in lines:
    count += 1
    split = line.split(" ")
    no_punct = ""
    for str in split:
        no_punct = ""
        for char in str:
            if char not in punctuations:
                no_punct = no_punct + char
        if no_punct.lower() in dic:
            print(no_punct)
            continue
        print(no_punct)
        option = input("Enter correction: \n")
        if option == "":
            continue
        no_punct = no_punct + " " + option + "\n"
        write.write(no_punct)
        write.flush()
