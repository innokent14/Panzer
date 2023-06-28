from config import *
from map import Map
import math
import pygame


class Panzer:
    def __init__(self, sc, color, start_pos, speed, size):
        self.x, self.y = start_pos
        self.sc = sc
        self.color = color
        self.speed = speed
        self.size = size
        self.a = [self.x, self.y, 0]

    def draw(self):
        pygame.draw.rect(self.sc, self.color, (self.x, self.y, self.size, self.size))

    def move(self, tile_list):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and\
                len(pygame.Rect(self.x, self.y-self.speed, self.size, self.size).collidelistall(tile_list)) == 0:
            self.y -= self.speed
        elif keys[pygame.K_s] and\
                len(pygame.Rect(self.x, self.y+self.speed, self.size, self.size).collidelistall(tile_list)) == 0:
            self.y += self.speed
        elif keys[pygame.K_a] and\
                len(pygame.Rect(self.x-self.speed, self.y, self.size, self.size).collidelistall(tile_list)) == 0:
            self.x -= self.speed
        elif keys[pygame.K_d] and\
                len(pygame.Rect(self.x+self.speed, self.y, self.size, self.size).collidelistall(tile_list)) == 0:
            self.x += self.speed

    def fire(self):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(self.sc, '#550000', (self.x + self.size//2, self.y + self.size//2), mouse_pos, 1)

        pygame.draw.circle(self.sc, '#789456', (self.a[0], self.a[1]), 20)

        self.a[0] += math.sin(mouse_pos[0])
        self.a[1] += math.sin(mouse_pos[1])


