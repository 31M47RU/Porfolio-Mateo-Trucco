import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("WindowKill Clone")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (100, 255, 100)

# Jugador
player_size = 40
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5
base_speed = 5  # Velocidad base

# Proyectiles
bullets = []
bullet_speed = 15
shooting = False  # Si está disparando

# Enemigos
enemies = []
enemy_health = 0
enemy_size = 30
enemy_speed = 5
spawn_timer = 0

# Tiempo para agrandar pantalla
expand_timer = 0
expand_interval = 600  # Cada 20 segundos (600 frames aprox)

# Reloj para FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    clock.tick(60)  # Limitar a 30 FPS
    screen.fill(WHITE)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:  # Detecta cuando la ventana cambia de tamaño
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            shooting = True
        if event.type == pygame.MOUSEBUTTONUP:
            shooting = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shooting = True
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            shooting = False

    # Controles
    keys = pygame.key.get_pressed()
    player_speed = base_speed * 2 if keys[pygame.K_LSHIFT] else base_speed  # Doble velocidad con Shift

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_r]:
        player_x, player_y = WIDTH // 2, HEIGHT // 2  # Reiniciar posición

    # Disparo continuo
    if shooting:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - player_y, mouse_x - player_x)
        bullet_dx = math.cos(angle) * bullet_speed
        bullet_dy = math.sin(angle) * bullet_speed
        bullets.append([player_x + player_size // 2, player_y, bullet_dx, bullet_dy])

    # Mover proyectiles
    for bullet in bullets:
        bullet[0] += bullet[2]  # Mueve en X
        bullet[1] += bullet[3]  # Mueve en Y
    bullets = [b for b in bullets if 0 < b[0] < WIDTH and 0 < b[1] < HEIGHT]

    # Generar enemigos
    spawn_timer += 1
    if spawn_timer > 30:
        enemy_x = random.choice([0, WIDTH - enemy_size])
        enemy_y = random.choice([0, HEIGHT - enemy_size])
        enemies.append([enemy_x, enemy_y])
        spawn_timer = 0

    # Mover enemigos hacia el jugador
    for enemy in enemies:
        angle = math.atan2(player_y - enemy[1], player_x - enemy[0])
        enemy[0] += math.cos(angle) * enemy_speed
        enemy[1] += math.sin(angle) * enemy_speed

    # Detectar colisiones
    for bullet in bullets:
        for enemy in enemies:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_size and
                    enemy[1] < bullet[1] < enemy[1] + enemy_size):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    # **Agrandar pantalla cada 20 segundos**
    expand_timer += 1
    if expand_timer >= expand_interval:
        WIDTH += 50
        HEIGHT += 50
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        expand_timer = 0

    # Dibujar jugador
    player = pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

    # Dibujar proyectiles
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 5, 10))

    # Dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Actualizar pantalla
    pygame.display.update()

pygame.quit()
