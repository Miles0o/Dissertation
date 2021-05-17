import cmudict

# flawer
# split up using sylables / vowls then look at the changes per vowl
# look for sylable differences

delimiter = ['a', 'e', 'i', 'o', 'u']

#learn change
def learn(input, output):
    # look for difference between two words
    # store difference
    return cmudict.dict().get(input)

#check for change
def predict(input, output):
    # word comes in check memory for like changes to make output
    # boost score
    return 0

# separate word into sylables
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



print(split_word("hello"))