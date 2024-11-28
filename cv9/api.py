import requests
response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()

total_people = len(data)
print(f"Celkem je v seznamu {total_people} lidí.")

first_person = data[0]
print("Informace o jednotlivých osobách:")
print(data[0].keys())

# Spočítáme muže a ženy
men = 0
women = 0
for person in data:
    if person["gender"] == "Male":
        men += 1
    elif person["gender"] == "Female":
        women += 1
print(f"V seznamu je {men} mužů a {women} žen.")