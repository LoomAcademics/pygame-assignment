import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Old School Video Game')

background_color = (180, 180, 180)

r1 = pygame.Rect(200, 100, 250, 50)
r2 = pygame.Rect(0, 0, 50, 250);

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    x, y = pygame.mouse.get_pos()
    r2.x = x
    r2.y = y

    c = (0, 0, 255)
    if r1.colliderect(r2):
        c = (255, 0, 0)

    pygame.draw.rect(screen, c, r1)
    pygame.draw.rect(screen, c, r2)

    pygame.display.update()
