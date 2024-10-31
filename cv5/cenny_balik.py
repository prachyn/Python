class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
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
    
class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f"Jeho hodnota je {self.value}"

    def delivery_price(self):
        pojisteni = self.value * 0.05
        zakladni_cena = super().delivery_price()
        return zakladni_cena + pojisteni

balik = Package("Kimova 12, Brno", 12, "Dorucen")
cenny_balik = ValuablePackage("Bohata 3, Praha", 44, "Nedoručen", 1000)

print(balik)
print(cenny_balik)
print(f"Cena dopravy vcetne pojisteni baliku je {cenny_balik.delivery_price()} Kč.")