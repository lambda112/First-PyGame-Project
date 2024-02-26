import pygame
from fighter import Fighter

pygame.init()

# Create Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")

# Set Framerate
clock = pygame.time.Clock()
FPS = 60

# Load background image
bg_image = pygame.image.load("assets\\images\\background\\street_fighter_fire.jpg").convert_alpha()

# Function for drawing background
def draw_bg(image, cordinates, size):
    scaled_bg = pygame.transform.scale(image, size)
    screen.blit(scaled_bg, cordinates)


# Create Two Instances of fighters
fighter_1 = Fighter(200, 450)
fighter_2 = Fighter(700, 450)


# Game Loop
run = True
while run:

    clock.tick(FPS)
    
    # Draw background
    draw_bg(image=bg_image, cordinates=(0,0), size =(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Move Fighters
    fighter_1.move(SCREEN_WIDTH)
    # fighter_2.move()

    # Draw Fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()

# Exit PyGame
pygame.quit()