def get_formatted_name(first_name, last_name):
    """Getting a clean formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.upper()

while True:
    print("\nPlease write your name:")
    print("(enter 'q' any time to quit)")

    f_name =input("Your First Name: ")
    if f_name == 'q':
        break
    l_name =input("Your Last Name: ")
    if l_name == 'q':
        break
    formated_name = get_formatted_name(f_name, l_name)
    print(f"\nhello ,{formated_name}")