import pygame, sys
from pygame.locals import *
from Projectile import *
from random import random
class Projectile:
    def __init__(self, x, y):
        self.color = (253, 204, 17)
        self.x = x
        self.y = y
        self.speed = -5
        self.isDead = False

    def update(self):
        self.y += self.speed
        if self.y <= self.speed:
            self.isDead = True

    def display(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y - self.speed))


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
        offset = self.w / 2
        pygame.draw.rect(screen, self.color, (self.x - offset, self.y, self.w, self.h))

class Invader:
    def __init__(self, x, y):
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.isDead = False

    def update(self):
        pass

    def display(self):
        pygame.draw.rect(screen, self.color, self.rect)

if __name__ == '__main__':
    pygame.init()

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Old School Video Game')
    clock = pygame.time.Clock()

    player = Spaceship()
    projectileList = []
    hasFired = False

    # Create Invaders
    invaderList = []
    for i in range(40):
        x = random() * width
        y = random() * height / 3

        invaderList.append(Invader(x, y))

    while True:
        # Re-initialize
        hasFired = False

        # Handle Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hasFired = True

        # Update logic
        player.update()
        if hasFired:
            projectileList.append(Projectile(player.x, 400))

        for i in invaderList:
            i.update()

        for p in projectileList:
            p.update()

            if p.isDead:
                projectileList.remove(p)

        for p in projectileList:
            for i in invaderList:
                if i.rect.collidepoint(p.x, p.y):
                    invaderList.remove(i)
                    projectileList.remove(p)
                    break

        # Display
        screen.fill((0, 0, 0))

        player.display()

        for i in invaderList:
            i.display()

        for p in projectileList:
            p.display()

        pygame.display.update()
        clock.tick_busy_loop(60)
