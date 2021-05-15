#read = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'r')
#master = open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r')
#write = open('/local_spellchecker/before fix.txt', 'a')

Lines = read.readlines()
check = master.readlines()
i = 0
for line in Lines:
    split = line.split(' ')
    split_check = check[i].split(' ')
    split[0] = split[0].lower()

    if split[1] != split_check[1]:
        #this should not happen, if it does the dictoneries are out of sync
        print('error' + split[1])
        break

    if "spellcor:" in split[0]:
        split[0] = split_check[0]

    write.write((split[0] + " " + split[1]))
    write.flush()
    i+=1



