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
        

frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nováková", "konstruktérka", 35)

print(frantisek.get_info())
print(klara.get_info())

#volani magicke metody __str__
print(klara)

print(klara.take_holiday(40))
print(klara.take_holiday(25))
print(klara.holiday_entitlement)