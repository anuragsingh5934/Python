# if condition

is_hot = True

if is_hot:
    print("Its's a hot day")
    print("Drink plenty of water")
else:
    print("It's cold day")
    print("Wear warm clothes")
print("Enjoy your day")


# it doesnt mean if there is not hot weather then it must be a cold,,
# making code more better
is_hot = False
is_cold = True

if is_hot:
    print("Its's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("\nIt's cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")