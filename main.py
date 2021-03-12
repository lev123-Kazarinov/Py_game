import pygame


class Ball():
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.color = (255, 0, 0)
        self.r = 50
        self.step_x = 0
        self.step_y = 0

    def move(self):
        self.x += self.step_x
        self.y += self.step_y

    def change_dir(self, step_x, step_y):
        self.step_x = step_x
        self.step_y = step_y

    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
first_ball = Ball((100, 100))
first_ball.change_dir(1, 1)
FPS = 1000
screen = pygame.display.set_mode((800, 600))
x, y = 100, 100
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    first_ball.update()
    first_ball.move()
    if first_ball.x + first_ball.r == 800 or first_ball.x - first_ball.r == 0:
        first_ball.change_dir(-first_ball.step_x, 0)
    if first_ball.y + first_ball.r == 600 or first_ball.y - first_ball.r == 0:
        first_ball.change_dir(0, -first_ball.step_y)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
