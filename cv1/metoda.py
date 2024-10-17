produkt = input("Zadej produkt: ")
produkt = produkt.lower() # VINO na vino

if produkt == "vino":
    print("vitej v kategorii vina")
elif produkt == "pivo":
    print("vitej v kategorii piva")
else:
    print("spatne zvolena hodnota")