import SuggestionWeigher
from local_spellchecker import Symspell
from Bing_API import API_talker
import json
import concurrent.futures
from local_spellchecker import adaptive



API = API_talker.API_talker()

executor = concurrent.futures.ThreadPoolExecutor()
thread1 = executor.submit(Symspell.symSpell,
                              ("D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt"))
thread2 = executor.submit(Symspell.symSpell,
                              ("D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt"))
speller = thread1.result()
Pon_Speller = thread2.result()
thread1.done()
thread2.done()

thread1.cancel()
thread2.cancel()

# translator for phonetic spellchecker
f = open('D:\github\Dissertation\local_spellchecker\\translator.json')
translator = json.load(f)
#print(API.API_call("so if i just type somthing out will you just work?"))

# word to be corrected
input_word = 'loanly'

# lookups
suggestions_sym = speller.lookup(input_word, 2)
suggestions_pho = Pon_Speller.lookup(input_word, 5)

# translator as well as lists of suggestions
master_list = SuggestionWeigher.suggestion_weigher(translator, suggestions_sym, suggestions_pho)

option = 1
for word in master_list:
    print(str(option) + ": " + str(word))
    option += 1
option = int(input("Enter option: \n"))
correction = master_list[option-1]

threshold = 0
if option > threshold:
    adaptive.adapt_controller(input_word, correction)





