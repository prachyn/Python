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
        else:
            return self.basic_price * 1.3
class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price + 2000 * self.checkout_luggages
        else:
            return self.basic_price * 1.5 + 2000 * self.checkout_luggages
vlak = TrainTicket(300, "2E", "business")
print(vlak.get_price())
letenka = PlaneTicket(5000, "2E", "business", 2)
print(letenka.get_price())