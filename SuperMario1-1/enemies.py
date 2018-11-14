import pygame
from pygame.sprite import Sprite
import spritesheet


class Enemies(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        ss = spritesheet.spritesheet('images/enemies.png')
        self.speed = 5.0

        # Goomba
        self.goombaleftimage = ss.image_at((0, 4, 16, 16), colorkey=(146, 39, 143))
        self.goombarightimage = ss.image_at((30, 4, 16, 16), colorkey=(146, 39, 143))
        self.goombasquishimage = ss.image_at((60, 8, 16, 16), colorkey=(146, 39, 143))
        self.image = pygame.transform.scale(self.rightimage2, (17 * 3, 17 * 3))
        self.rect = self.image.get_rect()

        # Koopa
        self.koopaleft1image = ss.image_at((150, 0, 16, 24), colorkey=(146, 39, 143))
        self.koopaleft2image = ss.image_at((180, 0, 16, 23), colorkey=(146, 39, 143))
        self.kooparight1image = ss.image_at((210, 0, 16, 23), colorkey=(146, 39, 143))
        self.kooparight2image = ss.image_at((240, 0, 16, 24), colorkey=(146, 39, 143))
        self.koopashell1image = ss.image_at((360, 5, 16, 14), colorkey=(146, 39, 143))
        self.koopashell2image = ss.image_at((330, 4, 16, 15), colorkey=(146, 39, 143))
        self.image = pygame.transform.scale(self.koopaleft1image, (17 * 3, 17 * 3))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
