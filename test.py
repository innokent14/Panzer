import math

from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x1, y1 = [WIDTH//2, HEIGHT//2]
a, b = WIDTH//2, HEIGHT//2
run = True
while run:
    screen.fill("#000011")
    event = pygame.event.get()

    for ev in event:
        if ev.type == pygame.QUIT:
            run = False
    x, y = pygame.mouse.get_pos()

    cof = (y1 - y) / ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
    pygame.draw.circle(screen, '#645964', (100, 100), 10)

    pygame.draw.circle(screen, '#645964', (a, b), 10)

    a += round(cof, 2) * 5
    b += round(cof, 2) * 5

    pygame.display.set_caption(f'FPS {round(clock.get_fps())}')
    pygame.display.update()
    clock.tick(FPS)
