#looping through all key value pairs
glossory = {
    'shampoo': 190,
    'oil': 140,
    'cream': 300,
    'deodrant': 510,
    'detergent': 320
}

for key, value in glossory.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")