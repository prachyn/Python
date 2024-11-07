class Employee:
    def __init__(self, name, position, holiday_entitlement):
        pass
    #name -> parametr metody, zanikne po opusteni metody
    #self.name -> atribut objektu, je svazan s objektem, hodnota zustane, dokud objekt nezanikne
    #potrebuju ulozit hodnotu z parametru name do atributu name
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
    def take_holiday(self, days):
        if days <= self.holiday_entitlement:
            self.holiday_entitlement = self.holiday_entitlement - days
            return "Užij si to"
        else:
            return "Na tolik dní nemáš nárok"
        
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízené."
class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)
        self.car = car        
        

frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nováková", "konstruktérka", 35)
marian = Manager("Marian Přísný", "Vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")

if isinstance(marian,Manager):
    print("Objekt pochází ze třídy Manager.")
else:
    print("Objekt nepochází ze třídy Manager.")

employe_list = [marian, klara, frantisek, marketa, jakub]
expected_people = 0

for item in employe_list:
    if isinstance(item,Manager):
        expected_people += 1

print(expected_people)

for item in employe_list:
    if hasattr(item,"car"):
        print(item.car)

prom = "car"
hodnota_atributu = getattr(marketa, prom, "nema autoXXX")
print(hodnota_atributu)
hodnota_atributu = getattr(frantisek, "car", "nema auto")
print(hodnota_atributu)

nazev_atributu  = input("Zadej nazev atributu: ")
hodnota_atributu = getattr(marketa, nazev_atributu, "u atributu neni zadna hodnota")
print(hodnota_atributu)