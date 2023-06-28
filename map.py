import pygame.draw
from config import *


class Map:
    def __init__(self, sc, _map, color):
        self.sc = sc
        self.map = _map
        self.color = color
        self.list = []
        self.tile = WIDTH // len(self.map[0])
        self.tile_list = []

    def init(self):
        for j, row in enumerate(self.map):
            for e, char in enumerate(row):
                if char == 'w':
                    self.list.append((e, j))

        for i in self.list:
            self.tile_list.append(pygame.Rect(i[0] * self.tile, i[1] * self.tile, self.tile, self.tile))

    def draw(self):
        for x, y in self.list:
            pygame.draw.rect(self.sc, self.color, (x * self.tile, y * self.tile, self.tile, self.tile), 1)




