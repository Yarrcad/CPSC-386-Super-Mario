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

    def update(self, modx):
        self.rect.centerx -= modx
