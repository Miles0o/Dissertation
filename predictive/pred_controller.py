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
            if len(syl) is 1:
                index += 1
                continue
            if syl not in output_syl[index]:
                if syl not in syl_corrections:
                    syl_corrections[syl] = [output_syl[index]]
                else:
                    if output_syl[index] not in syl_corrections[syl]:
                        syl_corrections[syl].append(output_syl[index])

            index += 1
        with open('D:\github\Dissertation\predictive\past_errors.json', 'w') as fp:
            json.dump(syl_corrections, fp)

# word comes in check memory for like changes to make output
# boost score
def predict(input, output):
    f = open('D:\github\Dissertation\predictive\past_errors.json')
    syl_corrections = json.load(f)
    input_syl, output_syl = split_word(input), split_word(output)

    if len(input_syl) == len(output_syl):
        index = 0
        for syl in input_syl:
            if syl is output_syl[index]:
                index += 1
                continue
            else:
                if syl in syl_corrections:
                    for corr in syl_corrections[syl]:
                        if corr in output_syl[index]:
                            return True
            index += 1
    return False

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

#print(predict("fluwer", "flower"))
#learn("fluwer", "flower")

