def build_person(first_name, last_name, age=None):
    """Return dictionry of information about a person"""
    person = {"first name": first_name, "last name": last_name}
    if age:
        person['age'] = age
    return person

person = build_person('sumit','sing')
print(person)