import math


class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


class Property:
    def __init__(self, locality):
        self.locality = locality


class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        estate_type_coefficients = {"land": 0.85,
                                    "building_site": 9,
                                    "forrest": 0.35,
                                    "garden": 2}

        return math.ceil(self.area * estate_type_coefficients[self.estate_type] * self.locality.locality_coefficient)


class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)        
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        coefficient = 1
        if self.commercial:
            coefficient = 2
        return math.ceil(self.area * self.locality.locality_coefficient * 15 * coefficient)

        
# Tvorim lokality a testuji
testlok = Locality('Testov',2)
testlok2 = Locality('Testov2',3)
manetin = Locality('Manětín', 0.8)
brno = Locality('Brno', 3)

# Tvorim nemovitosti
testprop = Estate(testlok, 'forrest', 500)
testbyt = Residence(testlok2, 60, False)
testbytpodnikani = Residence(testlok2, 60, True)
zempoz = Estate(manetin, 'land', 900)
dum = Residence(manetin, 120, False)
kancl = Residence(brno, 90, True)

# Pocitam
print(f"Farmland tax: {zempoz.calculate_tax()}")
print(f"House tax: {dum.calculate_tax()}")
print(f"Office tax: {kancl.calculate_tax()}")


print(f"Testovaci lokalita: {testprop.calculate_tax()}")
print(f"Testovaci byt false: {testbyt.calculate_tax()}")
print(f"Testovaci byt podnikani: {testbytpodnikani.calculate_tax()}")
