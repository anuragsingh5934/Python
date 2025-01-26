def greet_user():
    """Display a simple greeting"""
    print('hello user!')
greet_user()

# passing information to a function

def greet_user(username):
    """Display a simple greeting"""
    print(f"hello, {username.upper()}!")


greet_user("Rishu")

# Passing arguments
    # Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.upper()}.")

describe_pet('dog', 'lulli')

# multiple function calls
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.upper()}.")

describe_pet('cat', 'mew')
describe_pet('dog', 'rochak')

# order matters  in positional arguments




# keyword arguments ('name', 'value') pair pass to a function # abhi tk ye tha ki arguments ko shi se arrng kro nhi to vo glt lg jayenge to answer glt ayega
# but av aisa ni hai
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.upper()}.")

describe_pet(animal_type= 'hamster', pet_name= 'harry')
describe_pet(animal_type= 'dog', pet_name= 'rochak')

# Default Value ( you can define default value )

def describe_pet(pet_name= 'raja(default value)', animal_type ='dog(default value)'):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.upper()}.")
 
describe_pet('rochak1')
describe_pet('rochak2', 'wolf2')
describe_pet(pet_name='rochak', animal_type= 'lion3')
describe_pet()




describe_pet('hamster', 'harry') # positional argument
describe_pet(animal_type='hamster', pet_name='harry') #keyword arguments

# equivalent Function calls

#A dog name willie
describe_pet('Willie009')
describe_pet(pet_name='Willie009')
# use any calling style you want
describe_pet(pet_name='Raja', animal_type='cow')
describe_pet(animal_type='cow', pet_name='Raja')
describe_pet('limba', 'ox')# do consider positions of your values

#Avoiding argument error 
#def describe_pet(pet_name, animal_type):
    """Display information about pet"""
    #print(f"\nI have a {animal_type}.")
    #print(f"My {animal_type}'s name is {pet_name.upper()}.")
#describe_pet() # not able to find argument to fill their format 

#Return Values
