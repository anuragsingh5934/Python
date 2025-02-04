coordinates = (1, 2, 3)
# i want to multiply without unpacking

# 1st method

x = coordinates[0] * coordinates[1] * coordinates[2]
print(x)

# 2nd method 

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x * y * z)

# 3rd is unpacking method

x, y, z = coordinates
print( x * y * z + 1)
