"""If name is less than 3 characters long
    name must be at 3 characters
otherwise if it's more than 50 characters
    name can be a maximum of 50 characters 
name looks good!"""

name = input("Your name: ")
name_len = len(name)

if name_len < 3:
    print("Hey, Name must be at least 3 characers")
elif name_len < 50:
    print(f"Mr.{name} , Name looks good.")
else:
    print("Name can be Maximum of 50 characters")