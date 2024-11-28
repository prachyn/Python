with open("praha.txt", mode="r", encoding="utf-8") as soubor:
    slova_celkem = 0
    for radek in soubor:
        slova_na_radku = radek.split()
        pocet_slov_na_radku = len(slova_na_radku)
        print(f"Na řádku je {pocet_slov_na_radku} slov.")
        slova_celkem += pocet_slov_na_radku


    print(f"Celkem je v souboru {slova_celkem} slov.")


