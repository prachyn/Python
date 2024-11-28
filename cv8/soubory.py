with open("vykaz.txt", "r", encoding="utf-8") as file:
    vykaz = [int(radek) for radek in file]

print(vykaz)

celkova_vyplata = 0
hodinova_mzda = int(input("Zadej hodinovou mzdu:"))

for hodina in vykaz:
    celkova_vyplata = celkova_vyplata + (hodina * hodinova_mzda)

prumerna_vyplata = celkova_vyplata/12

print(f"Celkova vyplata je {celkova_vyplata} Kč")
print(f"Prumerna mesicni vyplata je {prumerna_vyplata} Kč")
