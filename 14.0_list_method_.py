# list method or list function
numbers = [5, 2, 1, 7, 4]

numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

# remove all items from a list
#numbers.clear()

# pop() , remove last items of the list
print(numbers.pop())

# finding index of the Number or available in list
  
print(numbers.index(1))
# 2

# "in" operator , for check item is present or not
print(50 in numbers) # its return boolean value

# counting a value in a list
print(numbers.count(5)) # 1 list me 5 , 1 hi baar hai to ye bs 1 show krega

# sorting a list
numbers = [5, 2, 1, 7, 4]
#print(numbers.sort())
numbers.sort()
print(numbers)

# reverse sorting

numbers = [5, 2, 1, 7, 4]
numbers.sort(reverse=True)
print(numbers)

# coping list , dependent to each other , non-dependent list
# dependent
numbers = [5, 2, 1, 7, 4]
number2 = numbers
numbers.append(30)
print(number2)

#  independent list
numbers = [5, 2, 1, 7, 4]
number2 = numbers.copy()
print(number2)