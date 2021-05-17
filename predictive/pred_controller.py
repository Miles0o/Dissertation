import json

# flawer
# split up using sylables / vowls then look at the changes per vowl
# look for sylable differences

delimiter = ['a', 'e', 'i', 'o', 'u']

# look for difference between two words
# store difference
def learn(input, output):
    f = open('D:\github\Dissertation\predictive\past_errors.json')
    syl_corrections = json.load(f)
    input_syl, output_syl = split_word(input), split_word(output)
    if len(input_syl) == len(output_syl):
        index = 0
        for syl in input_syl:
            if syl is not output_syl[index]:
                break

            #index += 1


        with open('D:\github\Dissertation\local_spellchecker\\translator.json', 'w') as fp:
            json.dump(syl_corrections, fp)

# word comes in check memory for like changes to make output
# boost score
def predict(input, output):

    return True

# separate word into sylables based on vowls
def split_word(word):
    split = []
    string = ""
    for letter in word:
        if letter in delimiter:
            split.append(string)
            string = ""
        string += letter
    if string != "":
        split.append(string)
    if split[0] == "":
        del split[0]
    return split



print(split_word("flawer"))

