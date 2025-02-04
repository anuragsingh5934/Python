weight = input("What is your weight (lbs or kg ): ")
lbs_kg = input("Press (l) for converting in lbs or (k) for converting in kg ")

if lbs_kg.lower() == 'l':
    converted_kg_to_lbs = int(weight) * 2.2
    converted_kg_to_lbs = round(converted_kg_to_lbs)
    print(f"Here is Your weight in Kg = {converted_kg_to_lbs}lbs")
if lbs_kg.lower() == 'k':
    converted_lbs_to_kg = int(weight) *   0.45359237
    converted_lbs_to_kg = round(converted_lbs_to_kg)
    print(f"Here is your weight in lbs = {converted_lbs_to_kg}kg")