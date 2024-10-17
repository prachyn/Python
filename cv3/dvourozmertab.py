books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

total_sales = 0
for item in books:
    print(item["price"])
    total_sales = total_sales + item["sold"] * item["price"]

print(f"Celkové tržby jsou {total_sales}")

#Trzby z roku 2019
total_sales = 0
for item in books:
    if item["year"] == 2019:
        print(item["price"])
        total_sales = total_sales + item["sold"] * item["price"]

print(f"Celkové tržby v roce 2019 jsou {total_sales}")
