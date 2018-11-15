import pygame
from pygame.sprite import Sprite


class Grouper(Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height)).convert()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.pier = False
        self.pier2 = False
        if self.x == 912 * 3:
            self.pier = True
        if self.x == 3600 * 3:
            self.pier2 = True

    def update(self, modx):
        self.rect.centerx -= modx
