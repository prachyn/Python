item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Název předmětu je Čajová konvička s hrnky
# Funguje ve verzi 3.12
print(f"Název předmětu je {item["title"]}")
# Funguje od verze 3.6
print(f"Název předmětu je {item['title']}")
item["weight"] = 0.8
key = "price"
item[key] = 929
print(item)
# Má item klíč weight?
if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není udána")


testslov = {"A", "B", "C", "D"}
print(len(testslov))
