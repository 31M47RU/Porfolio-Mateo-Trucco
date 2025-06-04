import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
ancho, alto = 600, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Gallina Esquiva Autos")

# Cargar imagen de fondo
fondo = pygame.image.load("images/caminotierra.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Reloj
reloj = pygame.time.Clock()

# Clase de la Gallina
class Gallina(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect(center=(ancho // 2, alto - 40))
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        mov_x, mov_y = 0, 0
        if teclas[pygame.K_a] and self.rect.left > 0:
            mov_x = -self.velocidad
        if teclas[pygame.K_d] and self.rect.right < ancho:
            mov_x = self.velocidad
        if teclas[pygame.K_w] and self.rect.top > 0:
            mov_y = -self.velocidad
        if teclas[pygame.K_s] and self.rect.bottom < alto:
            mov_y = self.velocidad

        # Normalizar velocidad en diagonal
        if mov_x != 0 and mov_y != 0:
            mov_x *= 0.7071
            mov_y *= 0.7071

        self.rect.x += int(mov_x)
        self.rect.y += int(mov_y)

# Clase de los Autos con efecto 3D
class Auto(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.image_base = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image_base, ROJO, [(15, 0), (30, 30), (0, 30)])
        self.image = self.image_base.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = velocidad

    def update(self):
        self.rect.y += self.velocidad
        escala = max(20, int(30 * (1 + (self.rect.y / alto))))
        self.image = pygame.transform.scale(self.image_base, (escala, escala))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.y))

        if self.rect.top > alto:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(50, ancho - 50)
            self.velocidad = random.randint(3, 7)

# Grupos de sprites
gallina = Gallina()
todos_sprites = pygame.sprite.Group()
autos = pygame.sprite.Group()

todos_sprites.add(gallina)

# Generar autos
for _ in range(5):
    x = random.randint(50, ancho - 50)
    y = random.randint(-100, -40)
    velocidad = random.randint(3, 7)
    auto = Auto(x, y, velocidad)
    todos_sprites.add(auto)
    autos.add(auto)

# Bucle principal
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualización
    todos_sprites.update()

    # Colisión solo cuando el auto está grande (cerca)
    for auto in autos:
        if auto.rect.colliderect(gallina.rect) and auto.rect.height > 40:
            print("¡Te atropellaron!")
            jugando = False

    # Dibujar en pantalla
    pantalla.blit(fondo, (0, 0))
    todos_sprites.draw(pantalla)
    pygame.display.flip()

    # Control de FPS
    reloj.tick(60)

pygame.quit()