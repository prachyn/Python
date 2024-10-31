class Package:
    def __init__(self, address, weight, state, driver):
        self.address = address
        self.weight = weight
        self.state = state
        self.driver = driver
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}"

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        return 359
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        self.state = "doručen"
        return "Doručení uloženo"
    def send_message(self):
        return f"Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: {self.driver.phone_number}"
    
class ValuablePackage(Package):
    def __init__(self, address, weight, state, value, driver):
        super().__init__(address, weight, state, driver)
        self.value = value
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state} a má hodnotu {self.value} Kč"
    
class Driver:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    def __str__(self):
        return f"Řidič {self.name} je k zastižení na čísle {self.phone_nuber}."
    
driver_1 = Driver("Jan Novák", "541 646 229")
driver_2 = Driver("Petr Parléř", "541 555 777")

package_1 = Package("Praha 1", 5.0, "nedorucen", driver_2)

print(package_1.send_message())