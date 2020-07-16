import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    if word in data:
        return data[word]
    if word.lower() in data:
        return data[word.lower()]
    if word.capitalize() in data:
        return data[word.capitalize()]
    if word.upper() in data:
        return data[word.upper()]
    else:
        return "Word not found."

def check_spell(word):
    if word in data:
        return word
    words_list = get_close_matches(word, data)
    for s in words_list:
        user_check = input("Did you mean: \"{}\" instead? [Y for YES / N for NO]: ".format(s))
        if user_check.lower() != "n":
            return s
    return "Word not found."

word = input("Word to check: ")
word = check_spell(word)
meaning = meaning(word)

if type(meaning) == list:
    print("{}:".format(word))
    i = 1
    for phrase in meaning:
        print("{}. {}".format(i, phrase))
        i += 1
else:
    print(word)

    

    