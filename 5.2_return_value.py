# topic - return value

# formated name 
def get_formatted_name(first_name, last_name):
    """Return full name , neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Practicing same code

def get_full_name(firstname, lastname):
    """full name of student"""
    fullname = f"{firstname} {lastname}"
    return fullname.upper()
student = get_full_name('raja', 'harishchandra')
print(student)