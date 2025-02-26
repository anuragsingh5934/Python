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

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back.")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()


'''Class	A blueprint/template for creating objects (e.g., Restaurant).
Instance	A specific object created from a class (e.g., restaurant).
Constructor (__init__)	A special method that initializes object attributes.
Attributes	Variables that store data about an object (e.g., restaurant_name, cuisine_type).
Methods	Functions inside a class that define object behavior (e.g., describe_restaurant(), open_restaurant()).
Instance Attribute	Attributes that belong to a specific object (e.g., self.restaurant_name).
Calling a Method	Using an object's function by writing object.method_name().'''