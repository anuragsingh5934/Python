def describe_pet(animal_type, pet_name): # parameter
    """Display info about pet"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()} name is {pet_name.upper()}.\n")

describe_pet('dog', 'simba') # argument 
describe_pet('dog', 'rochak')
describe_pet('cat', 'billo')
