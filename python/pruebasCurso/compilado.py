main = '''from robot import MyRobot
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
'''
matrix_functions = '''import random

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
'''
robot = '''from controller import Robot, Camera

class MyRobot:
    def __init__(self):
        self.robot = Robot()

        # Configurar ruedas
        self.wheel1 = self.robot.getDevice("wheel1")
        self.wheel2 = self.robot.getDevice("wheel2")

        # Configurar cámara frontal
        self.front_camera = self.robot.getDevice("camera1")
        self.front_camera.enable(10)

        # Otros sensores y actuadores pueden agregarse según sea necesario
        self.gyro = self.robot.getDevice("gyro")
        self.gps = self.robot.getDevice("gps")
        self.lidar = self.robot.getDevice("lidar")

    def get_camera_image(self):
        return self.front_camera.getImage()

    def move_forward(self, speed):
        self.wheel1.setVelocity(speed)
        self.wheel2.setVelocity(speed)

    def stop_motors(self):
        self.wheel1.setVelocity(0)
        self.wheel2.setVelocity(0)
'''

if __name__ == "__main__":
    # Itera sobre todas las variables globales
    for var_name, var_value in globals().items():
        # Verifica si la variable es una cadena y contiene ''' en su valor
        if isinstance(var_value, str) and "'''" in var_value:
            # Realiza el reemplazo y actualiza la variable
            globals()[var_name] = var_value.replace("'''", "")
    
    print(main, robot, matrix_functions)
