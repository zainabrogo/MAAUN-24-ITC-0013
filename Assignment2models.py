from abc import ABC, abstractmethod

# The Abstract Base Class
class StationAsset(ABC):
    @abstractmethod
    def calculate_revenue(self):
        """Method to be implemented by subclasses"""
        pass

class FuelDispenser(StationAsset):
    def __init__(self, liters_sold, price_per_liter):
        self.liters_sold = liters_sold
        self.price_per_liter = price_per_liter

    def calculate_revenue(self):
        # Logic: Total volume times price
        return self.liters_sold * self.price_per_liter

class CarWash(StationAsset):
    def __init__(self, number_of_washes, price_per_wash):
        self.number_of_washes = number_of_washes
        self.price_per_wash = price_per_wash

    def calculate_revenue(self):
        # Logic: Fixed fee per wash
        return self.number_of_washes * self.price_per_wash