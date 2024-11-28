import json
# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/json/format-json/transformace-dat
# Vytvořím si prázdný slovník, do kterého budu vytvářet požadovaný výstup
output = {}
with open("words.txt", encoding="utf-8") as file:
    # Otevřu si vstupní soubor a budu ho načítat v cyklu po řádcích
    for line in file:
        # Zbavím se znaku pro nový řádek v každém slově
        line = line.strip()
        # Zjistím si první písmeno slova
        first = line[0]
        # Pokud písmeno není klíčem slovníku, tak tento záznam vytvořím a jako hodnotu vložím seznam s tímto slovem
        if first not in output:
            output[first] = [line]
        # Jinak slovo připojím na konec existujícího seznamu slov
        else:
            output[first].append(line)
# Po zpracování celého vstupu seřadím seznamy slov na všech klíčích
for item in output:
    sorted(item)
# Výstupní slovník zapíšu do souboru ve formátu JSON
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4, sort_keys=True)