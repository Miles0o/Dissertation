import json
import SuggestionWeigher

ratio_num = 8348

def convert(suggs):
    suggestions = []

    for sug in suggs:
        # term, distance, count
        suggestions.append(SuggestionWeigher.SuggestItem(sug["suggestion"], 1, (float(sug["score"]) * ratio_num)))
    return suggestions

def ratio():
    dic = (open('D:\github\Dissertation\local_spellchecker\\frequency_dictionary_en_82_765.txt', 'r', errors='ignore'))
    f = open('D:\github\Dissertation\Bing_API\Bing_response.json')
    responses = json.load(f)
    lines = dic.readlines()
    total = 0
    count = 0
    for line in lines:
        line = line.strip('\n')
        test = line.split(" ")
        total += int(test[1])
        count += 1
    dic_av = total/count

    total = 0
    count = 0
    for element in responses:
        for sugg in responses[element]:
            count += 1

            total += float(sugg["score"])*1000
            print(total)
            print(sugg)

    av = int(total/count)
    print(dic_av/av)
