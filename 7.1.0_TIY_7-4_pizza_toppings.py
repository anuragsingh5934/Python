# pizza toppings
pizza_toppings = ''

while True:
    user_pizza = input("Write Your toppings :  ")
    pizza_toppings = user_pizza +" , "+ pizza_toppings
    if user_pizza.lower() == 'quit':
        break
    else:
        print(f"\nHere is your topping you want {pizza_toppings.upper()}")
