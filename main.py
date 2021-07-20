import pygame
from pygame.locals import *
from pygame import Color

# documentation: https://www.pygame.org/docs/index.html

################################################################################

pygame.init()

WIDTH, HEIGHT = 800, 600
TITLE = ""
FPS = 60
BACKGROUND = Color("black")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

################################################################################

running = True
while running:
    ### UPDATE ###
    delta = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    ### DRAW ###
    screen.fill(BACKGROUND)

    pygame.display.update()

pygame.quit()
