class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        Long_name = f"{self.year} {self.make} {self.model}"
        return Long_name.title()
    
    def read_odometer(self):
        """Print statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()