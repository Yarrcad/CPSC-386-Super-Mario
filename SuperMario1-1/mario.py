import pygame
from pygame.sprite import Sprite
import spritesheet


class Mario(Sprite):

    def __init__(self, screen, solids, bricks):
        super().__init__()
        self.screen = screen
        self.solids = solids
        self.bricks = bricks

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
        self.speed -= 1
        if self.speed == 0:
            self.index += 1
            if self.index == len(self.rimages):
                self.index = 0
            self.image = pygame.transform.scale(self.rimages[self.index], (15 * 3, 31 * 3))
            self.speed = 8
        self.rect.centerx += self.xvelo
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if solid.rect.left >= self.rect.right:
                self.rect.right = solid.rect.left - 1
                self.xvelo = 0
            if solid.rect.right <= self.rect.left:
                self.rect.left = solid.rect.right + 1
                self.xvelo = 0
        self.rect.centery -= self.yvelo
        if self.yvelo >= 19:
            self.jumping = False
        if not self.jumping:
            self.yvelo -= 2
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
<<<<<<< HEAD:SuperMario1-1 - Copy/mario.py
            if self.rect.centerx > solid.rect.right and self.rect.bottom < solid.rect.top:
                self.rect.left = solid.rect.right + 1
            elif self.rect.centerx < solid.rect.left and self.rect.bottom < solid.rect.top:
                self.rect.right = solid.rect.left - 1
            elif self.rect.centery > solid.rect.centery:
=======
            if solid.rect.bottom <= self.rect.top:
>>>>>>> d91a8e5aed99c79f76a09506118f8fcc28fe1b63:SuperMario1-1/mario.py
                self.rect.top = solid.rect.bottom + 1
                self.yvelo = 0
            elif solid.rect.top <= self.rect.bottom:
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
