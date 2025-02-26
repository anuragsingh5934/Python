def get_full_name(first_name, last_name):
    '''full name function'''
    fullname = f"{first_name.upper()} {last_name.upper()}"
    return fullname

while True:
    print("(Type 'q' for exit)")
    f_name = input("Enter Your First Name - :\n")
    if f_name == 'q':
        break

    l_name = input("Enter Your Last Name - :\n")
    if l_name == 'q':
        break
    break
student = get_full_name(f_name,l_name)
print(student)