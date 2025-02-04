def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
        
a = [1,5,3,22,45,11,43,2,36,77,32,11,23,12,5,3]
finding_max = find_max(a)
print(finding_max)