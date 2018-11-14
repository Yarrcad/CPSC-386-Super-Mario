import pygame
from pygame.sprite import Sprite
import spritesheet


class Goomba(Sprite):
    def __init__(self, screen, xpos):
        super().__init__()
        self.screen = screen
        ss = spritesheet.spritesheet('images/enemies.png')

        # Goomba
        self.goombaleftimage = ss.image_at((0, 4, 16, 16), colorkey=(146, 39, 143))
        self.goombarightimage = ss.image_at((30, 4, 16, 16), colorkey=(146, 39, 143))
        self.goombasquishimage = ss.image_at((60, 8, 16, 16), colorkey=(146, 39, 143))
        self.image = pygame.transform.scale(self.goombaleftimage, (17 * 3, 17 * 3))
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
