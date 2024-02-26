import pygame

pygame.init()

# Create Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")

# Game Loop
run = True
while run:

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Exit PyGame
pygame.quit()