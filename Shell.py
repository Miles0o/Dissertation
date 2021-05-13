from local_spellchecker import Symspell
from Bing_API import API_talker
API = API_talker.API_talker()

speller = Symspell.symSpell("D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt")
Pon_Speller = Symspell.symSpell("D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt")

for word in speller.lookup('loanly'):
    print(word)


##print(API.API_call("so if i just type somthing out will you just work?"))
