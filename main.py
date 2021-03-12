import pygame

pygame.init()
FPS = 1000
screen = pygame.display.set_mode((800, 600))
x, y = 100, 100
clock = pygame.time.Clock()
running = True
dir = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    if x + 50 == 800 or x - 50 == 0:
        dir = -1
    x += 1 * dir
    clock.tick(FPS)

    pygame.display.flip()

pygame.quit()
