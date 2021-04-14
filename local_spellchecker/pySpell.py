import time
from symspellpy import SymSpell, Verbosity

class pySpell:

    def __init__(self):
        #innitilisation
        self.sym_spell = SymSpell(max_dictionary_edit_distance=8, prefix_length=9)
        self.dictionary_path = "D:\github\Dissertation\\venv\Lib\site-packages\symspellpy\\frequency_dictionary_en_82_765.txt"
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        self.sym_spell.load_dictionary(self.dictionary_path, term_index=0, count_index=1)

    # lookup suggestions for single-word input strings
    def lookup(self, word):
        # max edit distance per lookup
        # (max_edit_distance_lookup <= max_dictionary_edit_distance)
        suggestions = self.sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        return suggestions

    def correctPhrase(self, sentance):
        # max edit distance per lookup
        # (max_edit_distance_lookup <= max_dictionary_edit_distance)
        suggestions = self.sym_spell.lookup_compound(sentance, max_edit_distance=8)
        return suggestions

