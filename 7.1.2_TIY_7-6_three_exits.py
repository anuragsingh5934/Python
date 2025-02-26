# movie tickets 
# school entry
school_entry = False
password = input("Enter Password : ")
if password.lower() == '123321':
    print("You are logged in !")
    school_entry = True
else:
    print("Login failed ! Please Try again.")

while school_entry == True:
    age = input("Enter Your child age : ")
    if age == "quit":
        print("Thank You for using software.")
        break
    elif int(age) < 3:
        print("Education free For Your Child.")
    elif int(age) < 10:
        print("Your fee for education is $10.")
    elif int(age) < 18:
        print("Your education fee is $15.")
    elif int(age) > 18:
        print("Fee is $20")
    else:
        print("Invalid input")