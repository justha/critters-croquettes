from datetime import date

class Horse:
    def __init__(self, name, species, shift):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = ""