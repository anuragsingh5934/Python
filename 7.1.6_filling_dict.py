contact_details = {}
software = False
login = input("ENTER USERNAME (case sensitive) : ")
if login == 'Rishu5934':
        password = input("ENTER PASSWORD : ")
        if password == '123321':
            print(f"logged in successfully\nWelcome {login}.")
            software = True
        else:
            print("Password is wrong. Please try again !")
else:
    print("Username not Found")

while software:
    name = input("What is your Name : ")
    contact_number = input("What is your Phone number : ")
    contact_details[name] = contact_number
    repeat = input("Do you want to save more contacts ? (y / n) : ")
    if repeat.lower() == 'n':
        print("Thank you for using software")
        see_contact = input("Do you want to see all saved contacts ? (y/ n) : ")
        if see_contact == 'y':
             print("----------CONTACT DETAILS----------")
             for name, contact in contact_details.items():
                print(f"Name {name} and phone number is {contact}")
        print("Thank you!")
        software = False