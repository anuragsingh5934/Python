# matrix = rectangular arrey of numbers

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# accessing a matrix
 
print(matrix[1][2])

# modifing value in matrixx

matrix[0][2] = 3
print(matrix[0][2])


for row in matrix:
    for item in row:
        print(item)