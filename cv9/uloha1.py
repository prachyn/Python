import json

finishers = []
with open("zavod.json", encoding="utf-8") as file:
    zavodnici = json.load(file)


for zavodnik in zavodnici:
   if zavodnik["casy"]["oficialni"] != "DNF":
       finishers.append([zavodnik["jmeno"], zavodnik["casy"]["oficialni"]])

print(finishers)

print(f"Stribrny zavodnik byl {finishers[1]} ")



