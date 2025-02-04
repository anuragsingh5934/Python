# removing duplicate in a list


numbers = [2, 2, 3, 5, 4, 6, 4]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)