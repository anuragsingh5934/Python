class Car:
    """car informantion details"""
    def __init__(self, name, model, year, cc, modification=''):
        if modification:
            self.name = name
            self.model = model
            self.year = year
            self.stock_cc = cc
            self.cc = cc
            self.modification = modification
            self.color = ''
        else:
            self.name = name
            self.model = model
            self.year = year
            self.cc = cc
            self.color = ''

    def full_name(self):
        """Returning a full name of car."""
        return f"The full name of car is {self.name} {self.model} {self.year}"
    
    def upgrade_cc(self, up_cc):
        """Upgrading cc of car"""
        if self.cc <= up_cc:
            print(f"Upgrading engine in your {self.name} from {self.stock_cc}cc to {self.cc}cc")
        else:
            print("you cant degrade your engine.")
    
    def update_car_color(self, usr_color):
        """Car color upgrade."""
        usr_color = self.color


my_car = Car('suzuki', 'swift', 2024, 1200)
updated_color = my_car.update_car_color('blue')
print(my_car.color)