import pygame
import pygame.font


class Startup:
    def __init__(self, screen):
        self.screen = screen
        self.menu_active = True
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)

        self.title = pygame.image.load_extended('images/title.png')
        self.title = pygame.transform.scale(self.title, (512, 256))
        self.titlerect = self.title.get_rect()

        self.play_button = self.font.render("Play", True, (255, 255, 255))
        self.playrect = self.play_button.get_rect()

        self.titlerect.center = self.screen_rect.center
        self.titlerect.y = 125

        self.playrect.center = self.screen_rect.center
        self.playrect.y = 471

    def blit(self):
        self.screen.blit(self.title, self.titlerect)
        self.screen.blit(self.play_button, self.playrect)
