import json
with open("absolventi.json", encoding="utf-8") as file:
    absolventi = json.load(file)
print(absolventi[0])

petr = absolventi[0]
print(petr["dochazka"]) # Vytahnuti hodnoty na zaklade klice


hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file) #zapisuju json
