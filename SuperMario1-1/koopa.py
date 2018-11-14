import pygame
from pygame.sprite import Sprite
import spritesheet


class Koopa(Sprite):
    def __init__(self, screen, xpos):
        super().__init__()
        self.screen = screen
        ss = spritesheet.spritesheet('images/enemies.png')
        self.koopaleft1image = ss.image_at((150, 0, 16, 24), colorkey=(146, 39, 143))
        self.koopaleft2image = ss.image_at((180, 0, 16, 23), colorkey=(146, 39, 143))
        self.kooparight1image = ss.image_at((210, 0, 16, 23), colorkey=(146, 39, 143))
        self.kooparight2image = ss.image_at((240, 0, 16, 24), colorkey=(146, 39, 143))
        self.koopashell1image = ss.image_at((360, 5, 16, 14), colorkey=(146, 39, 143))
        self.koopashell2image = ss.image_at((330, 4, 16, 15), colorkey=(146, 39, 143))
        self.image = pygame.transform.scale(self.koopaleft2image, (17 * 3, 17 * 3))
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.rect.x = xpos

        self.collidewithsolids = False

    def update(self, modx):
        if self.collidewithsolids:
            self.rect.x += modx
        else:
            self.rect.x -= modx

    def blit(self):
        self.screen.blit(self.image, self.rect)