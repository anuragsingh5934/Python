# use [] for list

# 1_list of Courses
courses = ['History', 'Maths', 'Physics', 'CompSci']

print(courses)

#2_indexing

print(courses[0])

#3_negative index

print(courses[-1]) #always last item like pop()

#4_index slicing

print(courses[0:2])
print(courses[:2])
print(courses[2:])
# also work in negative

#5_adding items in our list
# using .append() method - this method adds a value in last by default 

courses.append('Art')

# want to add value in a list on desired location use ----- insert(location , 'value') ------ method ..2 argumnt

courses.insert(0, 'Hindi')
print(courses)

# adding list in list

courses_2 = ['Geography', 'Education']

#using insert method

courses.insert(0, courses_2)
print(courses) 
# [['Geography', 'Education'], 'Hindi', 'History', 'Maths', 'Physics', 'CompSci', 'Art'] it added intr list , not value , this is not what we want
#it make ['Geography', 'Education'] as a first vaue

# here we we use extend() its work on item in a list
courses.remove(courses_2) # clearing insert code falut ..ignore this

courses.extend(courses_2)
print(courses)

#6_ removing items form a list ....................

# .remove('value') method
courses.remove('Maths')
print(courses)

# .pop() for last value of list and also return value if you set variables
courses.insert(2, 'Maths') # ignore
print(courses)

popped = courses.pop()
print(popped)

#7_Sorting and Reversing list 
courses.reverse()

courses.sort()
print(courses)

num = [1, 5, 4, 6, 2, 3]
num.sort()
print(num)

#sorting in decending order
num.sort(reverse=True)

# sorted function is for it sort items without affection original list
num = [1, 5, 4, 6, 2, 3]
sorted(num)
print(num) # [1, 5, 4, 6, 2, 3] bcz it not change orignl list 

sorted_num = sorted(num)
print(sorted_num) # yeh that is temp


#8_min, max, sum

print(min(num))
print(max(num))
print(sum(num))

#9_finding a index of a value
        #using Index('item') method

print(courses.index('CompSci'))
print(courses)

#10_Checking item present in a list or not , true false
print('Art' in courses)

#11_Looping

for item in courses:
    print(item)

#12_ Accesseing index of a item as well as item also ....use  enumerate()
for index, item in enumerate(courses): # gives us index and value
    print(index, item)

#0 Art
#1 CompSci
#2 Geography
#3 Hindi
#4 History
#5 Maths
#6 Physics
            # i want to strt form 1
for index, item in enumerate(courses, start=1): # gives us index and value
    print(index, item)

#13_seprting strings using .join('list') method
#split
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)