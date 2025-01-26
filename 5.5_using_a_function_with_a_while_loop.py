def get_formatted_name(first_name, last_name):
    """return full name , neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name 

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("last name: ")
    print("Welcome to pyhton course")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
    

