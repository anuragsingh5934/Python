# making argument optional , so people can choose to provide extra informantion only if they want to.
def get_fullname(first_name, last_name, middle_name=''):
    """Optional middle name , fill if you want to do so"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.upper()
stundent = get_fullname('suraj', 'shahu')

print(stundent)

worker = get_fullname('ram', middle_name='kumar', last_name='yadav')  

################# practicing 
def get_full_name(first, last, middle=''): # (_known as function's definition)
    """full name for us"""
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.capitalize()

managers_name = get_full_name('ramesh', 'kumar', 'chandra')
print(managers_name)