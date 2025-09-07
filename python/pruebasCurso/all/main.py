from robot import MyRobot
from matrix_functions import *

def main():
    my_robot = MyRobot()

    # Generar matriz original
    original_matrix = generate_matrix(rows=9, cols=14)

    print("Original:")
    for row in original_matrix:
        print(row)

    # Corregir matriz
    fixed_matrix = fix_matrix(original_matrix)

    print("\nCorregida:")
    for row in fixed_matrix:
        print(row)

    errors = compare_matrices(original_matrix, fixed_matrix)

    print("\nErrores:")
    for row in fixed_matrix:
        print(row)

    print(f"\nErrores: {errors}")

    # Ejemplo de movimiento hacia adelante
    my_robot.move_forward(2.0)

if __name__ == "__main__":
    main()
