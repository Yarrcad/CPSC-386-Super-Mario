import pygame
from pygame.sprite import Sprite
import spritesheet


class Coin(Sprite):

    def __init__(self, brick, type_):
        super().__init__()

        # 1 = static; 2 = brick coin
        self.index = 0
        self.brick = brick
        self.icounter = 4
        self.active = True
        self.index = 0
        self.type = type_
        self.stepcount = 10
        ss = spritesheet.spritesheet('images/items.png')
        self.bimages = ss.load_strip((0, 112, 16, 16), 4, (0, 0, 0))
        self.image = pygame.transform.scale(self.bimages[self.index], (16 * 3, 16 * 3))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.brick.rect.centerx
        self.rect.centery = self.brick.rect.centery

    def update(self, modx):
        self.icounter -= 1
        if self.icounter <= 0:
            self.index += 1
            if self.type == 2:
                if self.index >= len(self.bimages):
                    self.index = 0
            if self.type == 2:
                self.image = pygame.transform.scale(self.bimages[self.index], (16 * 3, 16 * 3))
            self.icounter = 4
        self.rect.centerx = self.brick.rect.centerx
        if self.type == 2:
            if self.stepcount > 0:
                self.stepcount -= 1
                self.rect.centery -= 8
            else:
                self.active = False
