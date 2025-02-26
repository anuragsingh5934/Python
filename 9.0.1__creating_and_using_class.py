class Dog:
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} roll over!")


my_dog = Dog('Rochak', 5)

print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old")

#accessing attributes
my_dog.name
# calling methods
my_dog.roll_over()
my_dog.sit()
