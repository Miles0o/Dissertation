import local_spellchecker

def suggestion_weigher(translator ,suggestion, suggestion_pho):
    master_suggestions_dic = {}

    #translate
    for word in suggestion_pho:
        value = (word.split(" "))[1]
        # true suggestions
        tru_sugg = translator[word]
        # add to suggestion list
        for word in tru_sugg:
            master_suggestions_dic[word] = int(value)

    # combine suggestion, if alredy present, increse frequency
    for word in suggestion:
        entrie = word.split(" ")

        if entrie[0] in master_suggestions_dic:
            master_suggestions_dic[entrie[0]] += int(entrie[1])
        else:
            master_suggestions_dic[word] = int(entrie[1])
