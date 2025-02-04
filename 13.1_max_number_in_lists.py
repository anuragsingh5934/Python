numbers  = [2, 4, 12, 3, 5, 23, 23, 554, 122, 5553, 1]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)