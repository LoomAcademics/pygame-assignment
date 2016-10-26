import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Old School Video Game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
