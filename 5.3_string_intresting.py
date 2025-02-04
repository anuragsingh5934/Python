course = 'Python for Beginners'
# calcu nuber of chrctr in string

# len() function , counting
print(len(course))

# (.) dot oprators use for get functions  method are use for string
# if any function belong to specific to any object then is called method
# .upper() fuction is specific to string , then we called this method

# upper() method
print(course.upper())
print(course.lower())
print(course.find('P')) # help to find index , we get -1 if we dont have any value in string which you try to find

print(course.find('Python')) # case sensetive hai sb kuch ,, start 0 se hai to answer v zero se dikhega

# using .replace() method in string
print(course.replace('P', 'J'))

# checking value is present or not ( outcome comes  in boolen )True or False
print('Python' in course)
print('python' in course)

# 'find' method returns index of the value whereas the 'in' oprator returns boolein _ true or false
