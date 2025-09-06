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
skin_color = (255, 222, 112)   # Color piel
contrast_color = (255, 156, 205) # Color contrastante (rosa claro)
transparent = (0, 0, 0, 0)

# Definir el jugador y el objetivo
player_radius = 10  # Reducido el radio a 5
player_x, player_y = 500, 500
player_speed = 50

target_size = 30
target_x, target_y = random.randint(0, 770), random.randint(0, 570)

# Mantener la ventana de Pygame en primer plano
pygame_window = gw.getWindowsWithTitle("Mi Juego")[0]
hwnd_pygame_window = pygame_window._hWnd

# Configurar la ventana en primer plano
ctypes.windll.user32.SetWindowPos(hwnd_pygame_window, ctypes.c_int(-1), 0, 0, 0, 0, 0x0001 | 0x0002)

extra_balls = []

# Flag para cambiar el color de la pantalla
change_color = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Puedes personalizar esta parte para mostrar un mensaje de salida, etc.
            print("¡No puedes cerrar la aplicación!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("¡No puedes cerrar la aplicación!")
                
    # Obtener la posición del mouse relativa a la ventana de Pygame
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Verificar si alguna pelota toca el mouse
    for ball in [pygame.math.Vector2(player_x, player_y)] + extra_balls:
        if pygame.math.Vector2(ball.x - mouse_x, ball.y - mouse_y).length() < player_radius:
            # Elegir un borde aleatorio para aparecer
            border = random.choice(['top', 'bottom', 'left', 'right'])

            # Calcular la posición inicial basada en el borde elegido
            if border == 'top':
                new_ball = pygame.math.Vector2(random.randint(0, pygame.display.get_surface().get_width()), 0)
            elif border == 'bottom':
                new_ball = pygame.math.Vector2(random.randint(0, pygame.display.get_surface().get_width()), pygame.display.get_surface().get_height())
            elif border == 'left':
                new_ball = pygame.math.Vector2(0, random.randint(0, pygame.display.get_surface().get_height()))
            elif border == 'right':
                new_ball = pygame.math.Vector2(pygame.display.get_surface().get_width(), random.randint(0, pygame.display.get_surface().get_height()))

            extra_balls.append(new_ball)

    # Mover al jugador hacia la posición del mouse de manera suavizada
    player_x += (mouse_x - player_x) * (player_speed * 0.001)
    player_y += (mouse_y - player_y) * (player_speed * 0.001)

    # Limpiar la pantalla
    if not change_color:
        pygame.display.get_surface().fill(transparent)
    change_color = False

    # Dibujar al jugador y al objetivo en la pantalla
    player = pygame.draw.circle(pygame.display.get_surface(), skin_color, (int(player_x), int(player_y)), player_radius)

    for ball in extra_balls:
        # Dibujar pene con testículos (círculo + rectángulo + dos círculos)
        pygame.draw.circle(pygame.display.get_surface(), skin_color, (int(ball.x), int(ball.y)), player_radius)
        pygame.draw.rect(pygame.display.get_surface(), skin_color, (int(ball.x - player_radius), int(ball.y), 2 * player_radius, 4 * player_radius))

        # Dibujar testículos
        pygame.draw.circle(pygame.display.get_surface(), contrast_color, (int(ball.x - player_radius), int(ball.y + 4 * player_radius)), player_radius)
        pygame.draw.circle(pygame.display.get_surface(), contrast_color, (int(ball.x + 2 * player_radius), int(ball.y + 4 * player_radius)), player_radius)

        # Mover la pelota hacia la posición del mouse de manera suavizada
        ball.x += (mouse_x - ball.x) * (player_speed * 0.001)
        ball.y += (mouse_y - ball.y) * (player_speed * 0.001)

    for event in pygame.event.get():
        if len(extra_balls) >= 25000:
                print(f"\n\n|||   LIMITE DE PITOS ALCANZADO   |||\nPitos: {len(extra_balls)}\n")
                pygame.quit()
                

    # Actualizar la pantalla principal
    pygame.display.flip()

    # Controlar la velocidad del bucle
   

    pygame.time.Clock().tick(60)
