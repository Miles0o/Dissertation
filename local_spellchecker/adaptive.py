import json

# if low on list add to translater and dictonery for refference ill pick below the top 5
# word is the misspelt string
# corrected would will be an SuggestItem object
def adapt(word, correct_word):

    # add new entry to dictonery
    write = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'a')
    write.write((word + " " + correct_word.count))

    # add new entrie to translator
    f = open('D:\github\Dissertation\local_spellchecker\\translator.json')
    translator = json.load(f)
    translator[word] = {correct_word}
    with open('D:\github\Dissertation\local_spellchecker\\translator.json', 'w') as fp:
        json.dump(translator, fp)


# word is a string of the correct word
def frequency_shift(word):

    read = open('D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt', 'r')
    write = open('D:\github\Dissertation\local_spellchecker\\before fix.txt', 'a')
    lines = read.readlines()

    total = 0
    for line in lines:
        words = line.split(' ')
        total += int(word[1])

    average_frequency = total/lines.count()
    line_number = 0

    # constant that determins how much a given word increses in frequency relative to average frequency
    k = 0.5
    for line in lines:
        line_number += 1
        words = line.split(" ")
        if word is words[0]:
            lines[line_number] = str(words[0] + " " + str(int(words[1]) + (average_frequency * k)))
