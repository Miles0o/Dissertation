import local_spellchecker
from symspellpy import SymSpell, Verbosity

def suggestion_compare(a, b):
    a = int((a.split(' '))[1])
    b = int((b.split(' '))[1])
    if a > b:
        return 1
    if a == b:
        return 0
    else:
        return-1

def suggestion_weigher(translator ,suggestion, suggestion_pho):
    master_suggestions_dic = {}

    #translate
    for word in suggestion_pho:
        print(word)
        # term, distance, count
        value = word.term()
        # true suggestions
        tru_sugg = translator[value]
        # add to suggestion list
        for words in tru_sugg:
            master_suggestions_dic[words] = SuggestItem(words, word.distance(), word.count())

    # combine suggestion, if alredy present, increse frequency
    for word in suggestion:
        entrie = word.term()

        if entrie in master_suggestions_dic:
            master_suggestions_dic[entrie].count(int(entrie.count()) + int(master_suggestions_dic[entrie].count()))
        else:
            master_suggestions_dic[word] = SuggestItem(words, word.distance(), word.count())

    master_suggestion = []

    # turn into a list to return
    for value in master_suggestions_dic:
        master_suggestion.append(str(value + " " + master_suggestions_dic[value]))
    master_suggestion.sort(suggestion_compare)
    return master_suggestion

class SuggestItem(object):
    def __init__(self, term, distance, count):
        self._term = term
        self._distance = distance
        self._count = count

    def term(self):
        return self._term

    def distance(self):
        return self._distance

    def count(self):
        return self._count

    def count(self, value):
        self._count = value



