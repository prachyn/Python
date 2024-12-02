import requests


def search_subject(ico: str) -> str:
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        obchodni_jmeno = data['obchodniJmeno']
        adresa = data['sidlo']['textovaAdresa']
        return f"{obchodni_jmeno}\n{adresa}"
    return f"Nepodarilo se najit subjekt s danym ICO: {ico}. Kód chyby: {response.status_code}"


def get_code_list() -> list:
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = {"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data = response.json()
        return data['ciselniky'][0]['polozkyCiselniku']
    return [f"Nepodařilo se stáhnout číselník právních forem. Kód odpovědi: {response.status_code}"]


def find_legal_form(code: str, code_list: list) -> dict:
    for item in code_list:
        if item['kod'] == code:
            return item['nazev'][0]
    return {"Chyba": "Neznámá právní forma"}


def search_subjects_by_name(subject_name) -> list:
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = {"obchodniJmeno": subject_name}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        results = []
        data = response.json()
        print(f"Nalezeno subjektů: {data['pocetCelkem']}")
        for subject in data['ekonomickeSubjekty']:
            legal_form_code = subject['pravniForma']
            legal_form = find_legal_form(legal_form_code, get_code_list())
            results.append(f"{subject['obchodniJmeno']}, {subject['ico']}, {legal_form['nazev']}")
        return results
    return [f"Nepodarilo se vyhledat. Kód chyby: {response.status_code}"]


def main():
    ico = input("Vložte ICO hledaného subjektu: ")
    print(search_subject(ico))

    subject_name = input("Vložte jméno subjektu: ")
    for subject in search_subjects_by_name(subject_name):
        print(subject)

main()
