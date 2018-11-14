import pygame
from pygame.sprite import Sprite
import spritesheet


class Mushroom(Sprite):

    def __init__(self, brick, bricks, solids):
        super().__init__()

        self.index = 16 * 3
        self.bricks = bricks
        self.solids = solids
        self.active = True
        self.brick = brick
        self.xvelo = 2
        self.yvelo = -1
        ss = spritesheet.spritesheet('images/items.png')
        self.rimage = pygame.transform.scale(ss.image_at((0, 0, 16, 16), (0, 0, 0)), (16 * 3, 16 * 3))
        self.image = self.rimage
        self.limage = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.left = self.brick.rect.left
        self.rect.top = self.brick.rect.top

    def update(self, modx):
        self.rect.centerx -= modx
        if self.index > 0:
            self.index -= 4
            self.rect.centery -= 4
        else:
            self.rect.centerx += self.xvelo
            solid = pygame.sprite.spritecollideany(self, self.solids)
            brick = pygame.sprite.spritecollideany(self, self.bricks)
            if solid:
                self.xvelo *= -1
                self.rect.right = solid.rect.left - 1
            if brick:
                self.xvelo *= -1
                self.rect.right = brick.rect.left - 1
            self.rect.centery -= self.yvelo
            solid = pygame.sprite.spritecollideany(self, self.solids)
            brick = pygame.sprite.spritecollideany(self, self.bricks)
            if solid:
                self.rect.bottom = solid.rect.top
                self.yvelo = -1
            elif brick:
                self.rect.bottom = brick.rect.top
                self.yvelo = -1
            else:
                self.yvelo -= 1
        if self.xvelo > 0:
            self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        else:
            self.image = self.limage
