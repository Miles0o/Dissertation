import time
from symspellpy import SymSpell, Verbosity

class symSpell:

    def __init__(self, path):
        #innitilisation
        #lowwer prefix number seems to have quicker load times
        #max edit distance affecs the max distance allowed, its kinda dumb ngl
        self.sym_spell = SymSpell(max_dictionary_edit_distance=6, prefix_length=7)
        self.dictionary_path = path
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        self.sym_spell.load_dictionary(self.dictionary_path, term_index=0, count_index=1)

    # lookup suggestions for single-word input strings
    def lookup(self, word, max):
        # max edit distance per lookup
        # (max_edit_distance_lookup <= max_dictionary_edit_distance)
        suggestions = self.sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=max)
        return suggestions

    def correctPhrase(self, sentance):
        # max edit distance per lookup
        # (max_edit_distance_lookup <= max_dictionary_edit_distance)
        suggestions = self.sym_spell.lookup_compound(sentance, max_edit_distance=6)
        return suggestions

