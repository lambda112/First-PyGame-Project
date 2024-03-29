import pygame

class Fighter():
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect((x,y, 80, 100))

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0

        # Get Keypresses
        key = pygame.key.get_pressed()

        # Movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED 

        # Ensure Player On Screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        # Update Player Position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)