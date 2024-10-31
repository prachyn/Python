class Package:
    def __init__(self, address, weight, state):
        pass
    #name -> parametr metody, zanikne po opusteni metody
    #self.name -> atribut objektu, je svazan s objektem, hodnota zustane, dokud objekt nezanikne
    #potrebuju ulozit hodnotu z parametru name do atributu name
        self.address = address
        self.weight = weight
        self.state = state
    
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} a je ve stavu {self.state}."
    
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} a je ve stavu {self.state}."

    def delivery_price(self):
        cena = 0
        if self.weight > 20:
            cena = 359
            return cena
        elif self.weight >= 10 and self.weight <= 20:
            cena = 159
            return cena
        elif self.weight < 10:
            cena = 129
            return cena
        
    def deliver_package(self):
        if self.state != "doručen":
            self.state = "doručen"
        else:
            print("Tento balíček byl již doručen")

balik1 = Package("Jindřišská 16, Praha 1", 12.1, "doručen")
balik2= Package("Klímova 14, Brno", 24.8, "nedoručen")

print(balik1.get_info())
print(balik1)
print(balik2.get_info())

print(balik1.delivery_price())
print(balik2.delivery_price())
balik2.deliver_package()
balik1.deliver_package()
print(balik2)


# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
# Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. Metoda spočítá cenu a vrátí ji jako číslo.