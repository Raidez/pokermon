import numpy as np
import pygame
from collections import namedtuple
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

class Card(pygame.Rect):
    size = (63, 88)
    ratio = 1.2

    def __init__(self, position):
        super().__init__(0, 0, 0, 0)
        self.width, self.height = tuple(np.array(Card.size) * Card.ratio)
        self.left, self.top = position
        self.color = Color("red")
        self.is_dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

Mouse = namedtuple("Mouse", ["x", "y"])

################################################################################

t = Card((WIDTH / 2, HEIGHT / 2))

running = True
while running:
    ### UPDATE ###
    delta = clock.tick(FPS)
    mouse = Mouse(*pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and t.collidepoint(event.pos):
            t.is_dragging = True
            dx, dy = t.x - mouse.x, t.y - mouse.y
        if event.type == pygame.MOUSEBUTTONUP:
            t.is_dragging = False
        if event.type == pygame.MOUSEMOTION and t.is_dragging:
            t.x, t.y = mouse.x + dx, mouse.y + dy
    
    ### DRAW ###
    screen.fill(BACKGROUND)

    t.draw(screen)

    pygame.display.update()

pygame.quit()
