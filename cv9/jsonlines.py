import json

absolvents = []
with open("absolventi2.jsonl", encoding="utf-8") as file:
    for line in file:
        # Při prvním běhu cyklu
        # line = {"name": "Gilbert", "session": "2013", "score": 24, "completed": true}
        # Ale line je str (řetězec)
        # current_absolvent je slovník
        # funkce loads převede řetězec na slovník
        current_absolvent = json.loads(line)
        absolvents.append(current_absolvent)
gilbert = absolvents[0]
print(gilbert["score"])