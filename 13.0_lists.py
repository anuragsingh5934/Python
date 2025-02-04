names = ['johan', 'bob', 'alex', 'iliyash', 'banta']

numbers = [1, 2, 5, 34 , 11, 545 , 23, 23,]
print(max(numbers))

# method 2

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)