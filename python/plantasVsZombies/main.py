import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Tamaño de la ventana y pantalla completa con bordes
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Plantas vs. Zombies Tutorial")

# Colores
brown = (165, 42, 42)
green = (0, 128, 0)
white = (255, 255, 255)

# Configuración del grid y jardín
cell_size = 50
grid_width, grid_height = screen_width // cell_size, screen_height // cell_size

# Inicializar el grid con tierra
grid = [[0] * grid_width for _ in range(grid_height)]

# Plantar algunas flores en el jardín
flowers = [(2, 3), (4, 7), (7, 5)]

for flower in flowers:
    grid[flower[1]][flower[0]] = 2  # Representación de una flor en el grid

# Objeto a mover
selected_object = None

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Cuando se hace clic, seleccionar objeto
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if screen_width // 4 <= mouse_x <= 3 * screen_width // 4 and screen_height // 4 <= mouse_y <= 3 * screen_height // 4:
                selected_object = ((mouse_x - screen_width // 4) // cell_size, (mouse_y - screen_height // 4) // cell_size)
        elif event.type == pygame.MOUSEMOTION and selected_object is not None:
            # Mover el objeto seleccionado con el mouse solo dentro del jardín
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if screen_width // 4 <= mouse_x <= 3 * screen_width // 4 and screen_height // 4 <= mouse_y <= 3 * screen_height // 4:
                grid[selected_object[1]][selected_object[0]] = 0  # Limpiar la posición anterior
                selected_object = ((mouse_x - screen_width // 4) // cell_size, (mouse_y - screen_height // 4) // cell_size)
                grid[selected_object[1]][selected_object[0]] = 1  # Colocar en la nueva posición

    # Dibujar el fondo marrón
    screen.fill(brown)

    # Dibujar el jardín (cuadro grande verde)
    pygame.draw.rect(screen, green, (screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2))

    # Dibujar la grilla dentro del jardín
    for y in range(grid_height):
        for x in range(grid_width):
            cell_x, cell_y = x * cell_size + screen_width // 4, y * cell_size + screen_height // 4
            pygame.draw.rect(screen, white, (cell_x, cell_y, cell_size, cell_size), 1)

    # Dibujar el jardín
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 1:
                pygame.draw.rect(screen, green, (x * cell_size + screen_width // 4, y * cell_size + screen_height // 4, cell_size, cell_size))  # Representación de una planta
            elif value == 2:
                pygame.draw.circle(screen, (255, 255, 0), (x * cell_size + screen_width // 4 + cell_size // 2, y * cell_size + screen_height // 4 + cell_size // 2), cell_size // 2)  # Representación de una flor

    pygame.display.flip()
