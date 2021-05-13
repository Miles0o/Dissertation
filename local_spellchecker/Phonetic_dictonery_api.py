from datamuse import datamuse
import json

api = datamuse.Datamuse()
#line = api.words(sp="won't", qe='sp', md='r', max=1)

read = open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r')
write = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'a')

#Lines = read.readlines()
Lines = ["hello 200", "flower 300", "flour 400"]
translator = {}
for line in Lines:

    split = line.split(' ')
    response = api.words(sp=split[0], qe='sp', md='r', max=1)
    ##with open('data.txt') as json_file:
        #response = json.load(json_file)
        #print(response)

    phon = response[0]['tags'][1]
    temp = phon.split(' ')
    temp[0] = temp[0].replace('pron:', '')
    newStr = ""
    for i in temp:
        newStr += str(i)
    result = ''.join([i for i in newStr if not i.isdigit()])
    if result not in translator.keys():
        translator[result] = [split[0]]
        write.write((result + " " + split[1]) + '\n')
    else:
        translator[result].append(split[0])




