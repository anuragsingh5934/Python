# keyvalue pair

customer = {
    "name": "john Smirh",
    "age": 20,
    "is_verified": True
}

customer["birthdate"] = "jan 1 1980" # adding key value
print(customer["name"])  # accessing  value
# print(customer[0]) You counter error!
# print(customer[school]) # not present in dictionaries , you face error message

# if we use .get() method , insted getting error we get none vlaue

print(customer.get('name')) 
print(customer.get('job'))

# adding in dict

customer['job'] = 'student'
print(customer.get('job'))
print(customer)