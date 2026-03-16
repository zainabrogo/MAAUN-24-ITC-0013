from datetime import datetime

class Business:
    def __init__(self, name, category, location):
        self.name = name
        self.category = category
        self.location = location
        self.date_added = datetime.now()

    def display(self):
        return f"{self.name} - {self.category} ({self.location})"