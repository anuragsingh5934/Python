# use {} for sets
# List of value, which is on order and not duplicated.
# sets remove Duplicates and shows random order every time when you execute.
# For a test A value is part of the set or not. sets do this thing more effectively than List and troubles. (membersip text)








# Checking a value which.shared with other.sets .

cs_courses = {'Art', 'CompSci', 'Geography', 'Hindi', 'History', 'Maths', 'Physics'}
art_courses = {'economics', 'CompSci', 'Geography', 'Hindi', 'agriculture', 'Maths', 'agronomy'}

print(cs_courses.intersection(art_courses)) # value commn in both

print(cs_courses.difference(art_courses)) # value in cs but not in art