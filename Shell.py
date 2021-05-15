import SuggestionWeigher
from local_spellchecker import Symspell
from Bing_API import API_talker
import json

API = API_talker.API_talker()

# generic spellchecker
speller = Symspell.symSpell("D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt")

# phonetic spellchecker
Pon_Speller = Symspell.symSpell("D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt")

# translator for phonetic spellchecker
f = open('D:\github\Dissertation\local_spellchecker\\translator.json')
translator = json.load(f)

# word to be corrected
word = 'loanly'

# lookups
suggestions_sym = speller.lookup(word)
suggestions_pho = Pon_Speller.lookup(word)

# translator as well as lists of suggestions
master_list = SuggestionWeigher.suggestion_weigher(translator, suggestions_sym, suggestions_pho)

for word in master_list:
    print(word)





#print(API.API_call("so if i just type somthing out will you just work?"))
