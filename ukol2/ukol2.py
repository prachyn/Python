import requests


def vyhledat_podnikatelsky_subjekt_ico():
    ico = input("Zadejte ICO: ")
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        obchodni_jmeno = data['obchodniJmeno']
        adresa = data['sidlo']['textovaAdresa']
        print(f"{obchodni_jmeno}\n{adresa}")
    else:
        print("Nepodarilo se najit subjekt s danym ICO.")

vyhledat_podnikatelsky_subjekt_ico()


def stahnout_ciselnik_pravnich_forem():
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        return data['ciselniky'][0]['polozkyCiselniku']
    else:
        print("Nepodařilo se stáhnout číselník právních forem.")
        return {}

ciselnik = stahnout_ciselnik_pravnich_forem()


def find_legal_form(kod, polozky_ciselniku):
    for polozka in polozky_ciselniku:
        if polozka['kod'] == kod:
            return polozka['nazev']
    return "Neznámá právní forma"


def vyhledat_podnikatelsky_subjekt_nazev():
    nazev = input("Zadejte cast nazvu subjektu: ")
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = f'{{"obchodniJmeno": "{nazev}"}}'
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        print(f"Nalezeno subjektů: {data['pocetCelkem']}")
        for subjekt in data['ekonomickeSubjekty']:
#            print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")
            pravni_forma_kod = subjekt['pravniForma']
            pravni_forma = find_legal_form(pravni_forma_kod, ciselnik)
            print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {pravni_forma[0]['nazev']}")
    else:
        print("Nepodarilo se vyhledat.")

vyhledat_podnikatelsky_subjekt_nazev()