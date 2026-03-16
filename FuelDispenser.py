class FuelDispenser:
    def __init__(self, liters_sold, price_per_liter):
        self.liters_sold = liters_sold
        self.price_per_liter = price_per_liter

    def calculate_revenue(self):
        return self.liters_sold * self.price_per_liter