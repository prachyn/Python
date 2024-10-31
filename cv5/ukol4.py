class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
        
# Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
# Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

# Přidej do výpisu informací o cenném balíku (metoda __str__) informaci o ceně balíku.
    def __str__(self):
        return super().__str__() + f" Jeho cena je {self.value}."
    
    def delivery_price(self):
        return super().delivery_price() + 0.05 * self.value

# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí. Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.
obycejny_balik = Package("Test", 20, "doručeno")
cenny_balik = ValuablePackage("Test 2", 12, "nedoručeno", 3020)

print(obycejny_balik)
print(cenny_balik)
print(cenny_balik.delivery_price())

# -----
# U cenných balíků bude k ceně připočteno pojištění. Přidej ke třídě ValuablePackage metodu delivery_price().
# Ta spočítá cenu přepravy s využitím metody mateřské třídy Package, kterou jsme vytvořili v předchozí lekci. K tomu připočte pojistné ve výši 5 % ceny balíku.



# Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sedadla). Tato třída bude sloužit například pro cesty autobusem.
class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

# Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu. Vytvoř třídu TrainTicket, která bude mít navíc atribut fare_class (uvažujeme možnosti economy a business).
class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

# Dále naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 30 % vyšší oproti basic_price,
# pokud fare_class je business.
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        # elif self.fare_class == "business": 
        #     return self.basic_price * 1.3
        else:
            return self.basic_price * 1.3

# U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. Vytvoř třídu PlaneTicket,
# která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, který udává počet odbavených zavazadel.
class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

# Naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy,
# a cenu o 50 % vyšší oproti basic_price, pokud fare_class je business. Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price + self.checkout_luggages * 2000
        # elif self.fare_class == "business": 
        #     return self.basic_price * 1.5  + self.checkout_luggages * 2000
        else:
            return self.basic_price * 1.5 + self.checkout_luggages * 2000

# Vytvoř jízdenku na vlak se základní cenou 150 do tříd economy i business. Zkontroluj, jakou hodnotu vrací metoda get_price().
jizdenka1_vlak = TrainTicket(150, 15, "economy")
jizdenka2_vlak = TrainTicket(150, 32, "business")

print(jizdenka1_vlak.get_price())
print(jizdenka2_vlak.get_price())

# Vytvoř letenku se základní cenou 6000 do tříd economy i business s jedním odbaveným zavazadlem. Zkontroluj, jakou hodnotu vrací metoda get_price().
letenka1 = PlaneTicket(6000, 156, "economy", 1)
letenka2 = PlaneTicket(6000, 201, "business", 1)

print(letenka1.get_price())
print(letenka2.get_price())

# Vyzkoušej vypočítat celkovou cenu dvou jízdenek různého typu, tj. jedné letenky a jedné jízdenky na vlak. Celkovou cenu ulož do proměnné total_price a k výpočtu použij metodu get_price().