def describe_pet(animal_type, pet_name): # parameter
    """Display info about pet"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()} name is {pet_name.upper()}.")

# keyword argument

describe_pet(animal_type= 'cat', pet_name= 'mufasa')

describe_pet(pet_name= 'raja ji', animal_type= 'dog')