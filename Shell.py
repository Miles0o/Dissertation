import SuggestionWeigher
from local_spellchecker import Symspell
from Bing_API import API_talker
import json
import concurrent.futures
from local_spellchecker import adaptive
from predictive import pred_controller
class shell:

    def __init__(self):
        API = API_talker.API_talker()

        executor = concurrent.futures.ThreadPoolExecutor()
        thread1 = executor.submit(Symspell.symSpell,
                                      ("D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt"))
        thread2 = executor.submit(Symspell.symSpell,
                                      ("D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt"))
        self.speller = thread1.result()
        self.Pon_Speller = thread2.result()
        thread1.done()
        thread2.done()

        thread1.cancel()
        thread2.cancel()

        # translator for phonetic spellchecker
        f = open('D:\github\Dissertation\local_spellchecker\\translator.json')
        self.translator = json.load(f)

    def lookup(self, input_word):
        #print(API.API_call("so if i just type somthing out will you just work?"))

        # word to be corrected
        input_word = 'flawer'

        # lookups
        suggestions_sym = self.speller.lookup(input_word, 2)
        suggestions_pho = self.Pon_Speller.lookup(input_word, 5)

        # translator as well as lists of suggestions
        master_list = SuggestionWeigher.suggestion_weigher(self.translator, suggestions_sym, suggestions_pho)

        # final prediction adjustments
        for sugg in master_list:
            if pred_controller.predict(input_word, sugg.term):
                sugg.count = int(sugg.count) * 1.5

        # user choice
        option = 1
        for word in master_list:
            print(str(option) + ": " + str(word))
            option += 1
        option = int(input("Enter option: \n"))
        correction = master_list[option-1]
        pred_controller.learn(input_word, correction)
        threshold = 5
        if option > threshold:
            adaptive.adapt_controller(input_word, correction)

        return correction





