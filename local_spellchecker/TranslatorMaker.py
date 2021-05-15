read = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'r')
master = open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r')

Lines = read.readlines()
check = master.readlines()
i = 0

translator = {}
for line in Lines:
    split = line.split(' ')
    split_check = check[i].split(' ')

    if split[0] not in translator:
        translator[split[0]] = [split_check[0]]
    else:
        translator[split[0]].append(split_check[0])
        
    i+=1