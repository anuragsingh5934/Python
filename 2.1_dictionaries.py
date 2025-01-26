# use {} = {'key': 'value'} and endless you add key value by seprating with ','
# comes with key value features

student = {'name': 'Rishu', 'age': 25, 'work': 'student','Courses': ['Maths', 'CompSci']} # = {'key': 'value', 'key': 'value'} **esme int aur list aur str sb contain ho jate hai
print(student['name'])                                                                    # = print(name_of_variable['key'])
print(student['age'])

# adding / modifing dec
# if key is not avlbl  ...
#print(student['phone']) # you get error message
 # for not get error use get() method
print(student.get('number'))  # non 
# you can define value which is not avl
print(student.get('number', 'there is no value'))

# new entry to dict

student['number'] = '9598658879' #new entry aur update dono krega ye method
print(student)

# updating
student['number'] = '0000000000'
print(student['number'])
print(student)

#update multiple value

student.update({'name': 'sumit', 'number': '0999098987', 'age': 26})
print(student)

# delet

del student['age']

# pop() method

age = student.pop('name')

print(student)

# loop through key and vlaue
#key  of dic
print(len(student))

#value of dic
print(student.values())

# key and value .items() method
print(student.items())

#looping
#not like list

for key in student:
    print(key) #wrong

for key, value in student.items():
    print(key, value)
