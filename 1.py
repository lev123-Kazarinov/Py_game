import pygame
import random

class Ball():
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50)
    pygame.display.flip()