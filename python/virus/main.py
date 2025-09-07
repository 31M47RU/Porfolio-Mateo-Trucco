import pygame
import random
import ctypes
import pygetwindow as gw

# Inicializar Pygame
pygame.init()

# Configurar el estilo para pantalla completa sin bordes
pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.FULLSCREEN)

# Obtener el identificador de la ventana de Pygame
hwnd = pygame.display.get_wm_info()["window"]

# Establecer la propiedad de transparencia de la ventana
ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea(hwnd, ctypes.byref(ctypes.c_int(-1)))

pygame.display.set_caption("Mi Juego")

# Colores
red = (255, 0, 0)

# Definir el jugador y el objetivo
player_radius = 10
player_x, player_y = 500, 500  # Cambié la posición inicial
player_speed = 20

target_size = 30
target_x, target_y = random.randint(0, 770), random.randint(0, 570)

# Lista para almacenar las pelotas adicionales
extra_balls = []

# Mantener la ventana de Pygame en primer plano
pygame_window = gw.getWindowsWithTitle("Mi Juego")[0]
hwnd_pygame_window = pygame_window._hWnd

# Configurar la ventana en primer plano
ctypes.windll.user32.SetWindowPos(hwnd_pygame_window, ctypes.c_int(-1), 0, 0, 0, 0, 0x0001 | 0x0002)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Obtener la posición del mouse relativa a la ventana de Pygame
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Verificar si la pelota principal toca el mouse
    if pygame.math.Vector2(player_x - mouse_x, player_y - mouse_y).length() < player_radius:
        # Crear una nueva pelota y agregarla a la lista
        new_ball = pygame.math.Vector2(player_x, player_y)
        extra_balls.append(new_ball)

    # Mover al jugador hacia la posición del mouse de manera suavizada
    player_x += (mouse_x - player_x) * (player_speed * 0.001)
    player_y += (mouse_y - player_y) * (player_speed * 0.001)

    # Limpiar la pantalla
    pygame.display.get_surface().fill((0, 0, 0, 0))

    # Dibujar al jugador y al objetivo en la pantalla
    pygame.draw.circle(pygame.display.get_surface(), (255, 0, 0, 255), (int(player_x), int(player_y)), player_radius)

    # Actualizar la posición de las pelotas adicionales y dibujarlas
    for ball in extra_balls:
        ball.x += (mouse_x - ball.x) * (player_speed * 0.001)
        ball.y += (mouse_y - ball.y) * (player_speed * 0.001)
        pygame.draw.circle(pygame.display.get_surface(), (255, 0, 0, 255), (random.randint(0, 770), random.randint(0, 570)), player_radius)

    # Actualizar la pantalla principal
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)