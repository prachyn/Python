sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for key in sales:
    print(key)

total_sales = 0
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
    total_sales = total_sales + value
    #total_sale += value

print(f"Celkem bylo prodáno {total_sales} výtisků.")