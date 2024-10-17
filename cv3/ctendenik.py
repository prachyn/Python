books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

#Napiš program, který spočte celkový počet stran, které Gustav přečetl.
#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
celkem_stran = 0
pocet_knih = 0
for item in books:
    celkem_stran += item["pages"]
    if item["rating"] >= 8:
        pocet_knih += 1
print(f"Gustav celkem precetl {celkem_stran} stran")
print(f"Pocet knih s hodnocenim alespon 8 je {pocet_knih}")
