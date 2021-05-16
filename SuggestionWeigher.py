import local_spellchecker
from symspellpy import SymSpell, Verbosity

def suggestion_compare(a, b):
    a1 = a.distance()
    a2 = a.count()
    b1 = b.distance()
    b2 = b.count()

    if (a1 > b1) or (a1 == b1 and a2 > b2):
        return 1

    if a1 == b1 and a2 == b2:
        return 0
    else:
        return-1

def suggestion_weigher(translator ,suggestion, suggestion_pho):
    master_suggestions_dic = {}

    #translate
    for word in suggestion_pho:
        # term, distance, count
        value = word.term
        # true suggestions
        tru_sugg = translator[value]
        # add to suggestion list
        for words in tru_sugg:
            master_suggestions_dic[words] = SuggestItem(words, word.distance, word.count)

    # combine suggestion, if alredy present, increse frequency
    for word in suggestion:
        entrie = word.term

        if entrie in master_suggestions_dic:
            count_value = (int(word.count) * int(master_suggestions_dic[entrie].count)
                           * (5 - int(master_suggestions_dic[entrie].distance)))
            master_suggestions_dic[entrie].count = count_value
        else:
            master_suggestions_dic[entrie] = SuggestItem(entrie, word.distance, word.count)

    master_suggestion = []

    # turn into a list to return
    for value in master_suggestions_dic:
        master_suggestion.append(master_suggestions_dic[value])
    master_suggestion.sort()
    return master_suggestion

class SuggestItem(object):
    def __init__(self, term, distance, count):
        self._term = term
        self._distance = distance
        self._count = count

    def __eq__(self, other):
        if self._distance == other.distance:
            return self._count == other.count
        else:
            return self._distance == other.distance

    def __lt__(self, other):
        if self._distance == other.distance:
            return self._count > other.count
        else:
            return self._distance < other.distance

    def __str__(self):
        return "{}, {}, {}".format(self._term, self._distance, self._count)

    @property
    def term(self):
        return self._term

    @property
    def distance(self):
        return self._distance

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value



