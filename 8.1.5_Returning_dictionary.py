def build_person(first_name, last_name):
    """Return a dictionary of information about person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('rishu', 'singh')
print(musician)