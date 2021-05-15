#read = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'r')
#write = open('D:\github\Dissertation\local_spellchecker\\before fix.txt', 'a')

Lines = read.readlines()
translator = {}
for line in Lines:
    split = line.split(' ')

    if split[0] not in translator:
        translator[split[0]] = int(split[1])
    else:
        translator[split[0]] += int(split[1])


for key in translator:
    write.write((key + " " + str(translator[key]) + "\n"))
    write.flush()
