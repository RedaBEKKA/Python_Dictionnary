import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(mot):
    mot = mot.lower()
    if mot in data:

        return data[mot]
    elif len(get_close_matches(mot,data.keys()))>0:
        yn= input(" Voulez vous dire %s a la place,dites O si oui ou N si non"%get_close_matches(mot,data.keys())[0])
        if yn == 'O':
            return data[get_close_matches(mot,data.keys())[0]]
        elif yn =="N":
            return "Mot n'existe pas ! "
        else:
            return "Nous n'avons pas compris votre réponce"
    else:
        return "le mot n'existe pas "



mot = input("entrer un mot SVp")
output = (translate(mot))
if type(output) == list:

    for item in output:
        print(item)
else:
    print(output)

