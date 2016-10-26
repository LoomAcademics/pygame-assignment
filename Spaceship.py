import pygame, sys
from pygame.locals import *



class Spaceship:
    def __init__(self):
        self.color = (255, 255, 255)
        self.x = 250
        self.y = 400
        self.w = 25
        self.h = 40

    def update(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))


if __name__ == '__main__':
    pygame.init()

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Old School Video Game')

    spaceship = Spaceship()

    while True:
        # Re-initialize

        # Handle Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update logic
        spaceship.update()

        # Display
        screen.fill((0, 0, 0));
        spaceship.display()
        pygame.display.update()
