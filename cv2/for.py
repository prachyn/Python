import statistics
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
podstatne_znamky = []
podstatne_predmety = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
for predmet in school_report:
    if predmet[0] in podstatne_predmety:
        podstatne_znamky.append(predmet[1])
        print(podstatne_znamky)
prumer_znamek = statistics.mean(podstatne_znamky)