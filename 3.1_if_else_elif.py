if True:
    print('Conditional was True')

if False:
    print('Conditional was False')

language = 'Python' 
if language == 'Python':
    print('Conditional was True 2')

# Comparisons:
# Equal:             ==
# Not Equal:         !=
# Greater Than:      >
# Less Than:         <
# Greater or Equal:  >=
# Less or Equal:     <=
# Object Identity:   is (checking value same id)
# True / False is known as boolen

language = 'Python' 
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')

language = 'Java' 
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')

# multiple checking 

language = 'Java' 
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

# talking about
# and
# or
# not

# and
user = 'admin'
logged_in = True

if user =='admin' and logged_in: # dono condition check krega
    print('Admin page')

# or 

user = 'Guest'
logged_in = True

if user =='admin' or logged_in: # dono me se 1 condition check krega agar koe 1 shi hua to exicute kr dega .
    print('Admin page')

# not (use for switch boolein)

user = 'admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

# is ( ye check krta h ki same id pe save hai data ki nhi )
a = [1, 2, 3]
b = [1, 2, 3] # ye dono list dikhne me same hai but id enka alag hai
print(a==b) # sb andr ki value same hai to == esko true kr dega
print(id(a))
print(id(b)) # yaha dono ki id alag hai ab 'is' esko check krta hai

print(a is b) # false aa gya 

# true k liye

b = [1, 2, 3]
a = b
print(a is b)
# or we can say
print(id(a) == id(b)) # what acctually is oprator do

print(id(a))
print(id(b))

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example {}

#####################################################
Condition = False

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')


Condition = True

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')

#######################################################
# False Values:
# False
# None                                            These are all false Value if you put in condition
# Zero of any numeric type . any other digit will be count in true
# Any empty sequence. For example, '', (), [].
# Any empty mapping/dict. For example {}
#######################################################
Condition = None

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')
########################################################
Condition = 0

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')

Condition = 1

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')
########################################################
Condition = ''

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')


Condition = 'Rishu'

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')
#########################################################
Condition = {}

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')


Condition = {'name': 'rishu'}

if Condition:
    print('Evaluated to True')
else:
    print('Evaluated to false')
###########################################################
