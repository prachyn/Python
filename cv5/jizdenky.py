class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class
 
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        elif self.fare_class == "business":
            return self.basic_price * 1.3

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)  
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        zavazadla = self.checkout_luggages * 2000
        if self.fare_class == "business":
            return super().get_price() * 1.5 + zavazadla
        else: return super().get_price() + zavazadla

vlak = TrainTicket(150, "22", "economy")
print(vlak.get_price())
letenka = PlaneTicket(5000, "2E", "business", 2)
print(letenka.get_price())