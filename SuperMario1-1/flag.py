import pygame
from pygame.sprite import Sprite
import spritesheet


class Flag(Sprite):

    def __init__(self):
        super().__init__()

        # 1 = normal; 2 = brick coin 3 = coin; a5 = mushroom 6 = star;
        self.bumped = False
        self.counter = 0
        self.icounter = 4
        self.active = True
        self.spent = False
        self.animate = True
        self.index = 0
        self.type = type_
        self.cvalue = 0
        if self.type == 1 or self.type == 2:
            ss = spritesheet.spritesheet('images/1-1.png')
            self.image = pygame.transform.scale(ss.image_at((1504, 136, 16, 16)), (16 * 3, 16 * 3))
        else:
            ss = spritesheet.spritesheet('images/items.png')
            self.images = ss.load_strip((0, 80, 16, 16), 4)
            self.image = pygame.transform.scale(self.images[self.index], (16 * 3, 16 * 3))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self, modx):
        if self.type != 1 and self.animate and self.type != 2:
            self.icounter -= 1
            if self.icounter <= 0:
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = pygame.transform.scale(self.images[self.index], (16 * 3, 16 * 3))
                self.icounter = 4
        elif self.type != 1 and self.type != 2:
            self.image = pygame.transform.scale(self.images[2], (16 * 3, 16 * 3))
        self.rect.centerx -= modx
        if self.bumped:
            if self.type != 1 and self.type != 2:
                self.animate = False
            self.counter += 1
            if self.counter <= 5:
                self.rect.centery -= 2
            elif self.counter <= 10:
                self.rect.centery += 2
            else:
                self.counter = 0
                self.bumped = False