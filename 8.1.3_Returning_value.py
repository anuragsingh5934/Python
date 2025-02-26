def get_formatted_name(first_name, last_name):
    """Returnting full name"""
    full_name = f"Mr/Miss {first_name} {last_name}"
    return full_name.title()

student = get_formatted_name('sumit', 'singh')
print(student)