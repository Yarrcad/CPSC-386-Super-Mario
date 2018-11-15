import pygame
from pygame.sprite import Sprite
import spritesheet


class Goomba(Sprite):
    def __init__(self, screen, xpos, ypos, solids, bricks):
        super().__init__()
        self.screen = screen
        ss = spritesheet.spritesheet('images/enemies.png')

        # Goomba
        self.goombaleftimage = pygame.transform.scale(ss.image_at((0, 4, 16, 16), colorkey=(146, 39, 143)),
                                                      (17 * 3, 17 * 3))
        self.goombarightimage = pygame.transform.scale(ss.image_at((30, 4, 16, 16), colorkey=(146, 39, 143)),
                                                       (17 * 3, 17 * 3))
        self.goombasquishimage = pygame.transform.scale(ss.image_at((60, 8, 16, 16), colorkey=(146, 39, 143)),
                                                        (17 * 3, 17 * 3))
        self.image = self.goombaleftimage
        self.rect = self.image.get_rect()
        self.img = 'l'
        self.rect.bottom = ypos * 3
        self.rect.left = xpos * 3
        self.active = False
        self.solids = solids
        self.bricks = bricks
        self.delay = 8
        self.squish = False
        self.xvelo = -2
        self.yvelo = -1
        self.rid = False

    def update(self, modx, maxx):
        self.rect.centerx -= modx
        if self.rect.left <= maxx + 980:
            self.active = True
            if self.active:
                if not self.squish:
                    self.delay -= 1
                    if self.delay <= 0:
                        self.delay = 8
                        if self.img == 'l':
                            self.image = self.goombarightimage
                            self.img = 'r'
                        elif self.img == 'r':
                            self.image = self.goombaleftimage
                            self.img = 'l'
                    self.rect.centerx += self.xvelo
                    solid = pygame.sprite.spritecollideany(self, self.solids)
                    brick = pygame.sprite.spritecollideany(self, self.bricks)
                    if solid:
                        self.xvelo *= -1
                        if self.rect.centerx < solid.rect.centerx:
                            self.rect.right = solid.rect.left - 1
                        else:
                            self.rect.left = solid.rect.right + 1
                    if brick:
                        self.xvelo *= -1
                        if self.rect.centerx < brick.rect.centerx:
                            self.rect.right = brick.rect.left - 1
                        else:
                            self.rect.left = brick.rect.right + 1
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
                else:
                    self.image = self.goombasquishimage
                    self.delay -= 1
                    if self.delay <= 0:
                        self.rid = True

    def blit(self):
        self.screen.blit(self.image, self.rect)
