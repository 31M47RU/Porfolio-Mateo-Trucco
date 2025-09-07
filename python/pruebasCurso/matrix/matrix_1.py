import random

def genMatrix(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def fixMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) - 1:
                matrix[row][col] = 1
    return matrix

def compMatrix(original, modificada):
    errors = 0
    for row in range(1, len(original) - 1):
        for col in range(1, len(original[0]) - 1):
            if original[row][col] != modificada[row][col]:
                errors += 1
                modificada[row][col] = "📍"
            else:
                modificada[row][col] = "👍"
    return errors

originalMatrix = genMatrix(rows=9, cols=14)

print("Original:")
for row in originalMatrix:
    print(row)

ficedMatrix = fixMatrix(originalMatrix)

# modified_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
# [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
# [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
# [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
# [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
# [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
# [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

print("\nArreglada:")
for row in ficedMatrix:
    print(row)

errores = compMatrix(originalMatrix, ficedMatrix)

print("\nErrores:")
for row in ficedMatrix:
    print(row)

print(f"""
||:----------------------------------------------------------::||
||:            Errores:            ||            {errores}           ::||
||:----------------------------------------------------------::||
""")
