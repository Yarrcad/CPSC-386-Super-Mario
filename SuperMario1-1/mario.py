import pygame
from pygame.sprite import Sprite
import spritesheet


class Mario(Sprite):

    def __init__(self, screen, solids, bricks, game):
        super().__init__()
        self.screen = screen
        self.solids = solids
        self.bricks = bricks
        self.game = game

        ss = spritesheet.spritesheet('images/mario.png')
        self.rimages = ss.images_at(((97, 1, 15, 31), (114, 1, 15, 31), (131, 1, 16, 31)), colorkey=(146, 39, 143))

        self.image = pygame.transform.scale(self.rimages[0], (15 * 3, 31 * 3))
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.ducking = False
        self.grounded = True
        self.index = 0
        self.speed = 8
        self.xspeed = 8
        self.xvelo = 0
        self.yvelo = 0
        self.xp = False
        self.jumping = False
        self.recent = None

    def update(self):
        self.game.xmod = 0
        self.speed -= 1
        if self.speed == 0:
            self.index += 1
            if self.index == len(self.rimages):
                self.index = 0
            self.image = pygame.transform.scale(self.rimages[self.index], (15 * 3, 31 * 3))
            self.speed = 8
        if self.rect.centerx < 490 or self.xvelo < 0:
            self.rect.centerx += self.xvelo
        else:
            self.game.modx = self.xvelo
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if self.rect.centerx < solid.rect.centerx:
                self.rect.right = solid.rect.left - 1
                self.xvelo = 0
            if self.rect.centerx > solid.rect.centerx:
                self.rect.left = solid.rect.right + 1
                self.xvelo = 0
        self.rect.centery -= self.yvelo
        if self.yvelo >= 19:
            self.jumping = False
        if not self.jumping:
            self.yvelo -= 2
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if self.rect.centery > solid.rect.centery:
                self.rect.top = solid.rect.bottom + 1
                self.yvelo = 0
            elif self.rect.centery < solid.rect.centery:
                self.rect.bottom = solid.rect.top - 1
                self.grounded = True
                self.yvelo = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.xvelo = 0
        if not self.xp:
            self.xspeed -= 1
            if self.xspeed == 0:
                if self.xvelo > 0:
                    self.xvelo -= 2
                elif self.xvelo < 0:
                    self.xvelo += 2
                self.xspeed = 8

    def blitme(self):
        self.screen.blit(self.image, self.rect)
