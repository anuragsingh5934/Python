# a function can return any kind of value you need  it to,  including more complex data structures like list and dictionaries

def build_persion(first_name, last_name):
    """Return a dictionary of informantion anout a persion"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_persion('jimmi' ,'singh')
print(musician)

# practice

def name_of_person(first_name, last_name, middle_name):
    """return dictionary"""
    if middle_name:
        person = {'first': first_name, 'middle': middle_name, 'last': last_name}
    else:
        person = {'first': first_name, 'last': last_name}
    return person

guest = name_of_person('raju', 'roy', 'gupta') 
print(guest)

guest = name_of_person(first_name='raju', middle_name='roy', last_name='gupta',)
print(guest)

def buil_person(first_name, last_name, age=None)
    ''''''
    person = {first_name, last_name}
    if age:
        person['age'] = age
        return person
    
musician = buil_person('jimmi', 'hindrix', age=27)
