person = {
    'name': 'aniruddha',
    'age': 24,
    'hobby': 'singer',
    'occupation': 'studying'
}
print(person['name'])
print(person['age'])
print(person.get('hobby', 'no information available'))
print(person.get('seeking', 'no_data_available_regard_seeking'))