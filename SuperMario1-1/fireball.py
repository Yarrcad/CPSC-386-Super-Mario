import pygame
from pygame.sprite import Sprite
import spritesheet


class Fireball(Sprite):

    def __init__(self, mario, solids, bricks):
        super().__init__()
        self.mario = mario
        self.solids = solids
        self.bricks = bricks

        ss = spritesheet.spritesheet('images/items.png')
        self.mimages = ss.images_at(((96, 144, 7, 7), (104, 144, 7, 7), (96, 152, 7, 7), (104, 152, 7, 7)),
                                    colorkey=(0, 0, 0))
        self.dimages = ss.images_at(((97, 1, 17, 31), (114, 1, 17, 31), (131, 1, 16, 31)), colorkey=(146, 39, 143))

        if self.mario.recent == 'd':
            self.xvelo = 12
        else:
            self.xvelo = - 12
        self.yvelo = 6
        self.active = True
        self.image = pygame.transform.scale(self.mimages[0], (7 * 3, 7 * 3))
        self.rect = self.image.get_rect()
        self.rect.centery = self.mario.rect.centery
        if mario.recent == 'd':
            self.rect.centerx = self.mario.rect.right
        else:
            self.rect.centerx = self.mario.rect.left
        self.ispeed = 4
        self.index = 0
        self.ycount = 2
        self.bound = False

    def update(self, modx):
        if self.yvelo < 6 and self.bound:
            self.ycount -= 1
            if self.ycount <= 0:
                self.yvelo += 1
                self.ycount = 2
        else:
            self.yvelo += 1
            self.bound = False
        if self.active:
            self.ispeed -= 1
            if self.ispeed <= 0:
                self.ispeed = 4
                self.index += 1
                if self.index >= len(self.mimages):
                    self.index = 0
                self.image = pygame.transform.scale(self.mimages[self.index], (7 * 3, 7 * 3))
        self.rect.centerx += self.xvelo - modx
        solid = pygame.sprite.spritecollideany(self, self.solids)
        brick = pygame.sprite.spritecollideany(self, self.bricks)
        if solid or brick:
            self.active = False
        self.rect.centery += self.yvelo
        solid = pygame.sprite.spritecollideany(self, self.solids)
        brick = pygame.sprite.spritecollideany(self, self.bricks)
        if solid:
            self.rect.bottom = solid.rect.top - 1
            self.yvelo = -6
            self.bound = True
        if brick:
            self.rect.bottom = brick.rect.top - 1
            self.yvelo = -6
            self.bound = True
