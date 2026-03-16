class CarWash:
    def __init__(self, number_of_washes, price_per_wash):
        self.number_of_washes = number_of_washes
        self.price_per_wash = price_per_wash

    def calculate_revenue(self):
        return self.number_of_washes * self.price_per_wash