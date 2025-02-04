# DRY   dont repeat yourself
# inheritance code ko repeate hone se bachata hai

# class Dog:
#     def walk(self):
#         print("walk")

# class Cat:
#     def walk(self):
#         print("walk") 
#                            This is wrong method ,, dont repeat the code

# ab hm parent class banayenge , taki code repeat  na ho

class Mammal:           # PARENT CLASS
    def walk(self):
        print("walk")

class Dog(Mammal):      # CHILD CLASS
    pass

class Cat(Mammal):      # CHILD CLASS
    pass

# Creating instances of Dog and Cat
dog1 = Dog()
cat1 = Cat()

# Using the inherited method
dog1.walk()  # Output: walk
cat1.walk()  # Output: walk