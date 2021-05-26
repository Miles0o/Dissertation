import SuggestionWeigher
from local_spellchecker import Symspell
from Bing_API import API_talker
import json
import concurrent.futures
from local_spellchecker import adaptive
from predictive import pred_controller
from Bing_API import Bing_conversion

class shell:

    def __init__(self):
        API = API_talker.API_talker()

        executor = concurrent.futures.ThreadPoolExecutor()

        thread2 = executor.submit(Symspell.symSpell,
                                      ("D:\github\Dissertation\local_spellchecker\Phonetc_dictonary.txt"))

        self.Pon_Speller = thread2.result()
        f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
        self.responses = json.load(f)

        thread2.done()
        thread2.cancel()

        # translator for phonetic spellchecker
        f = open('D:\github\Dissertation\local_spellchecker\\translator.json')
        self.translator = json.load(f)

    def lookup(self, input_word, output_word):
        #print(API.API_call("so if i just type somthing out will you just work?"))

        # word to be corrected
        #input_word = 'flawer'

        # lookups
        if input_word in self.responses:
            suggestions_Bing = Bing_conversion.convert(self.responses[input_word])
        else:
            suggestions_Bing = {}
        suggestions_pho = self.Pon_Speller.lookup(input_word, 5)

        # translator as well as lists of suggestions
        master_list = SuggestionWeigher.suggestion_weigher(self.translator, suggestions_Bing, suggestions_pho)

        # final prediction adjustments
        for sugg in master_list:
            if pred_controller.predict(input_word, sugg.term):
                sugg.count = int(sugg.count) * 1.5

        # user choice
        option = 0
        found = 0
        for word in master_list:
            if word.term == output_word:
                found = 1
                break
            #print(str(option) + ": " + str(word))
            option += 1

        if found == 0:
            if len(master_list) == 0:
                print(input_word)

            return input_word

        correction = master_list[option]
        pred_controller.learn(input_word, correction.term)
        threshold = 5
        if option > threshold:
            adaptive.adapt_controller(input_word, correction)

        return correction.term





