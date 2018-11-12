import pygame
from pygame.sprite import Sprite
import spritesheet


class Fflower(Sprite):

    def __init__(self, brick):
        super().__init__()

        self.index = 16 * 3
        self.active = True
        self.brick = brick
        ss = spritesheet.spritesheet('images/items.png')
        self.image = ss.image_at((48, 32, 16, 16), (0, 0, 0))
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.brick.rect.centerx
        self.rect.centery = self.brick.rect.centery
    def update(self, modx):
        self.rect.centerx -= modx
        if self.index > 0:
            self.index -= 4
            self.rect.centery -= 4