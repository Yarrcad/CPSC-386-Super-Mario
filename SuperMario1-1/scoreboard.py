import pygame
import pygame.font


class Scoreboard:

    def __init__(self, screen):
        self.score = 0
        self.coins = 0
        self.lives = 3
        self.time = 400
        self.font = pygame.font.SysFont(None, 36)
        self.font_color = (255, 255, 255)
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.levelname = self.font.render('1-1', True, self.font_color)
        self.world = self.font.render('WORLD', True, self.font_color)
        self.world_rect = self.world.get_rect()
        self.ln_rect = self.levelname.get_rect()
        self.world_rect.y = 20
        self.world_rect.x = 600
        self.ln_rect.y = 40
        self.ln_rect.x = 600
        self.delay = 16

        self.coin_display = pygame.image.load_extended('images/coin.png')
        self.coin_display = pygame.transform.scale(self.coin_display, (32, 32))
        self.coin_rect = self.coin_display.get_rect()
        self.coin_rect.y = 20
        self.coin_rect.x = 450
        self.coins_val = None  # rect to hold number of coins collected
        self.coin_vrect = None  # will hold number of coins collected

        self.score_key = None  # Used to display score title
        self.score_val = None  # used to display actual player score
        self.score_krect = None  # Rect for score title
        self.score_vrect = None  # rect for actual score

        self.time_key = None
        self.time_val = None
        self.time_krect = None
        self.time_vrect = None

        self.lives_key = None
        self.lives_val = None
        self.lives_krect = None
        self.lives_vrect = None

        self.update()

    def reset_stats(self):
        self.score = 0
        self.coins = 0
        self.lives = 3
        self.time = 400

    def update(self):
        self.delay -= 1
        if self.delay <= 0:
            self.time -= 1
            self.delay = 16
        self.score_key = self.font.render("SCORE", True, self.font_color)
        self.time_key = self.font.render("TIME", True, self.font_color)
        self.lives_key = self.font.render("LIVES", True, self.font_color)
        self.score_val = self.font.render(str(self.score), True, self.font_color)
        self.time_val = self.font.render(str(self.time), True, self.font_color)
        self.coins_val = self.font.render(str(self.coins), True, self.font_color)
        self.lives_val = self.font.render(str(self.lives), True, self.font_color)

        self.score_krect = self.score_key.get_rect()
        self.time_krect = self.time_key.get_rect()
        self.score_vrect = self.score_val.get_rect()
        self.time_vrect = self.score_val.get_rect()
        self.coin_vrect = self.coins_val.get_rect()
        self.lives_krect = self.lives_key.get_rect()
        self.lives_vrect = self.lives_val.get_rect()

        self.score_krect.left = self.screen_rect.left + 20
        self.score_krect.top = 20
        self.time_krect.left = self.screen_rect.left + 300
        self.time_krect.top = 20
        self.score_vrect.left = self.screen_rect.left + 20
        self.score_vrect.top = 40
        self.time_vrect.left = self.screen_rect.left + 300
        self.time_vrect.top = 40
        self.coin_vrect.top = 25
        self.coin_vrect.x = 490
        self.lives_krect.left = 800
        self.lives_krect.top = 20
        self.lives_vrect.left = 800
        self.lives_vrect.top = 40
    def blit(self):
        self.screen.blit(self.score_key, self.score_krect)
        self.screen.blit(self.score_val, self.score_vrect)

        self.screen.blit(self.time_key, self.time_krect)
        self.screen.blit(self.time_val, self.time_vrect)

        self.screen.blit(self.coin_display, self.coin_rect)
        self.screen.blit(self.coins_val, self.coin_vrect)

        self.screen.blit(self.world, self.world_rect)
        self.screen.blit(self.levelname, self.ln_rect)

        self.screen.blit(self.lives_key, self.lives_krect)
        self.screen.blit(self.lives_val, self.lives_vrect)
