from datamuse import datamuse
import json

api = datamuse.Datamuse()
#line = api.words(sp="won't", qe='sp', md='r', max=1)

#read = open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r')
#write = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'a')

Lines = read.readlines()
#Lines = ["hello 200", "flower 300", "flour 400"]
translator = {}
count = 0
for line in Lines:
    count += 1
    split = line.split(' ')
    response = api.words(sp=split[0], qe='sp', md='r', max=1)
    phon = response[0]['tags'][1]
    temp = phon.split(' ')
    temp[0] = temp[0].replace('pron:', '')
    print(str(count) + "/82781: " + temp[0])
    newStr = ""
    for i in temp:
        newStr += str(i)
    result = ''.join([i for i in newStr if not i.isdigit()])
    write.write((result + " " + split[1]))
    write.flush()




