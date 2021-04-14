from local_spellchecker import pySpell
from Bing_API import API_talker
API = API_talker.API_talker()
speller = pySpell.pySpell()

for word in speller.correctPhrase('hollo worlb'):
    print(word)
#print(API.API_call("so if i just type somthing out will you just work?"))
