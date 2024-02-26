import pygame

pygame.init()

# Create Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")


# Load background image
bg_image = pygame.image.load("assets\\images\\background\\street_fighter_fire.jpg").convert_alpha()

# Function for drawing background
def draw_bg(image, cordinates, size):
    scaled_bg = pygame.transform.scale(image, size)
    screen.blit(scaled_bg, cordinates)

# Game Loop
run = True
while run:
    
    # Draw background
    draw_bg(image=bg_image, cordinates=(0,0), size =(SCREEN_WIDTH, SCREEN_HEIGHT))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()

# Exit PyGame
pygame.quit()