import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Old School Video Game')

background_color = (180, 180, 180)

r1 = pygame.Rect(200, 100, 250, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    c = (0, 0, 255)

    if r1.collidepoint(pygame.mouse.get_pos()):
        c = (255, 0, 0)

    pygame.draw.rect(screen, c, r1)

    pygame.display.update()
