from controller import Robot, Camera

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
