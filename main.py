from panzer import Panzer
from map import Map
from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


map_1 = Map(screen, [
    'wwwwwwwwwwwwwwww',
    'w......w.......w',
    'w.......w..w...w',
    'w..w....w...w..w',
    'w......w.......w',
    'w..............w',
    'w...w..........w',
    'w......w.......w',
    'w.......w...w..w',
    'w..w....w......w',
    'w......w.......w',
    'wwwwwwwwwwwwwwww',
], '#548567')

tank_1 = Panzer(screen, '#115511', (WIDTH//2, HEIGHT//2), 5, 20)
map_1.init()



run = True
while run:
    screen.fill("#000011")
    event = pygame.event.get()

    tank_1.draw()
    tank_1.move(map_1.tile_list)
    map_1.draw()
    if pygame.mouse.get_pressed()[0]:
        tank_1.fire()

    for ev in event:
        if ev.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pygame.display.set_caption(f'FPS {round(clock.get_fps())}')
    clock.tick(FPS)
