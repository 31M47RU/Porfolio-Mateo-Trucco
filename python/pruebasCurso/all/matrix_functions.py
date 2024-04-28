import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def fix_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) - 1:
                matrix[row][col] = 1
    return matrix

def compare_matrices(original, modified):
    errors = 0
    for row in range(1, len(original) - 1):
        for col in range(1, len(original[0]) - 1):
            if original[row][col] != modified[row][col]:
                errors += 1
                modified[row][col] = "📍"
            else:
                modified[row][col] = "👍"
    return errors
