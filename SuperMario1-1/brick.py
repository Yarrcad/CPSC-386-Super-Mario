import pygame
from pygame.sprite import Sprite
import spritesheet


class Brick(Sprite):

    def __init__(self, x, y, type):
        super().__init__()

        # 1 = normal; 2 = coin; 3 = fire flower; 4 = mushroom;
        self.type = type
        if self.type == 1:
            ss = spritesheet.spritesheet('images/items.png')
            self.image = pygame.transform.scale(ss.image_at((0, 80, 15, 15)), (15 * 3, 15 * 3))
        else:
            ss = spritesheet.spritesheet('images/items.png')
            self.images = ss.load_strip((0, 80, 15, 15), 4)
            self.image = pygame.transform.scale(self.images[0], (15 * 3, 15 * 3))
        self.image = pygame.Surface((15, 15)).convert()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
