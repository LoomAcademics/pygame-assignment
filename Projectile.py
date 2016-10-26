import pygame, sys
from pygame.locals import *

class Projectile:
    def __init__(self, x, y):
        self.color = (253, 204, 17)
        self.x = x
        self.y = y
        self.speed = -5

    def update(self):
        self.y += self.speed

    def display(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y - self.speed))


if __name__ == '__main__':
    pygame.init()

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Old School Video Game')
    clock = pygame.time.Clock()

    p = Projectile(250, 400)

    while True:
        # Re-initialize

        # Handle Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update logic
        p.update()

        # Display
        screen.fill((0, 0, 0))
        p.display()

        pygame.display.update()
        clock.tick_busy_loop(20)
