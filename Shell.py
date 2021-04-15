from local_spellchecker import pySpell
from Bing_API import API_talker
API = API_talker.API_talker()
speller = pySpell.pySpell()

for word in speller.lookup('loanly'):
    print(word)
#print(API.API_call("so if i just type somthing out will you just work?"))
