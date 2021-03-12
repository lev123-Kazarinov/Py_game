import pygame
import random


class Ball():
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.color = (255, 0, 0)
        self.r = 50
        self.step_x = random.randint(0, 5)
        self.step_y = random.randint(0, 5)

    def move(self):
        self.x += self.step_x
        self.y += self.step_y

    def change_dir(self, step_x, step_y):
        self.step_x = step_x
        self.step_y = step_y

    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
x, y = random.randint(100, 200), random.randint(100, 200)
list_ball = [Ball((x, y)) for i in range(3)]
FPS = 10
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for bal in list_ball:
        print(bal.x, bal.y, bal.r, bal.step_x, bal.step_y)
        bal.update()
        bal.move()
        if bal.x + bal.r >= 800 or bal.x - bal.r <= 0:
            bal.change_dir(-bal.step_x, bal.step_y)
        if bal.y + bal.r >= 600 or bal.y - bal.r <= 0:
            bal.change_dir(bal.step_x, -bal.step_y)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
