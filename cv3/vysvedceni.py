school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

#Napiš program, který spočte průměrnou známku ze všech předmětů.
pocet = 0
soucet_znamek = 0
for predmet, znamka in school_report.items():
    soucet_znamek += znamka
    pocet += 1

prumer = soucet_znamek / pocet
print(f"Prumer znamek je {prumer}")
#Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for predmet, znamka in school_report.items():
    if znamka == 1:

        print(predmet)

#METODA Values

