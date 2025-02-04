# more advance than function

# class is a blueprint for creating object
 
# insistance = object

class Student:
    name = 'karan kumar'

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

#crating a class
class Car:
    color = "blue"
    brand = "mercedes"


# creating object
car1 = Car() # ye car ka object hai
print(car1.brand)


# __init__ function (constructur)

class Student:
    college = 'abc college'              # class attribute
    def __init__(self, fullname):
        self.name = fullname            # object attribute
        print('adding new student in data base...')


s1 = Student('karan')
print(s1.name) # karan

s2 = Student('arjun')     #arjun attributes bolte hai
print(s2.name)

