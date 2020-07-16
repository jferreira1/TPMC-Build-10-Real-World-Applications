import mysql.connector 
from difflib import SequenceMatcher, get_close_matches

con = mysql.connector.connect(
user = "ardit700_student", 
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

def check_spell(word, expressions):
    if (word in expressions) or (word.lower() in expressions) or (word.capitalize() in expressions) or (word.upper() in expressions):
        return word
    else:
        words_list = get_close_matches(word, expressions)
        for s in words_list:
            user_check = input("Did you mean: \"{}\" instead? [Y for YES / N for NO]: ".format(s))
            if user_check.lower() != "n":
                return s
            else:
                return word

def meaning(word, expressions):
    if (word in expressions) or (word.lower() in expressions) or (word.capitalize() in expressions) or (word.upper() in expressions):
        cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}'".format(word))
        result = cursor.fetchall()
        return result
    else:
        return "Word not found."
    

cursor = con.cursor()
cursor.execute("SELECT Expression FROM Dictionary")
expressions = cursor.fetchall()
expressions = set([exp[0] for exp in expressions])


word = input("Word to check: ")
word = check_spell(word, expressions)
results = meaning(word, expressions)



if type(results) == list:
    print("{}:".format(word))
    i = 1
    for result in results:
        print("{}. {}".format(i, result[0]))
        i += 1
else:
    print("Word not found.")