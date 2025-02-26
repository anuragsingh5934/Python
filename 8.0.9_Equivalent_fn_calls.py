def describe_pet(animal_type, pet_name, vaccinated='no'): # parameter
    """Display info about pet"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()} name is {pet_name.upper()}.")
    print(f"Vaccination- {vaccinated.upper()}")

# equivalent function calls -
describe_pet('dog', 'simba') # argument 
describe_pet('cat', 'raga', 'yes')
describe_pet(vaccinated='yes', pet_name='sobha', animal_type='cow') 