import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 128, 0)
CARD_FONT = pygame.font.Font(None, 36)

# Creación de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Función para crear una baraja de cartas
def crear_baraja():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Función para dibujar una carta
def draw_card(x, y, carta):
    card_text = CARD_FONT.render(carta, True, (0, 0, 0))
    screen.blit(card_text, (x, y))

# Inicialización del juego
baraja = crear_baraja()
random.shuffle(baraja)
jugador = []
dealer = []

# Repartir cartas iniciales
for _ in range(2):
    jugador.append(baraja.pop())
    dealer.append(baraja.pop())

# Loop principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibuja el fondo
    screen.fill(BACKGROUND_COLOR)

    # Dibuja las cartas del jugador
    for i, carta in enumerate(jugador):
        draw_card(100 + i * 100, 300, carta)

    # Dibuja una carta del dealer boca arriba
    draw_card(100, 100, dealer[0])
    
    pygame.display.flip()

# Cierre de Pygame
pygame.quit()
sys.exit()
