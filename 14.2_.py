numbers = [1, 1, 5, 4, 2, 5, 1, 5, 7, 8, 3, 1, 8, 1]

new_number = []

for number in numbers:
    #print(number)
    if number not in new_number:
        new_number.append(number)
print(new_number)