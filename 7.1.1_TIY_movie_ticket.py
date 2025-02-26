#Movie ticket
ticket = True

while ticket:
    print("Hint - 0 for 'quit'")
    value = input("Your age : ")
    age = int(value)
    if age == 0:
        print("Thank you for using application")
        break
    elif age < 12:
        print("Ticket price is $10.")
    elif age > 12:
        print("Ticket price is $15.")