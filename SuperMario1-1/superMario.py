import pygame
from level import Level
import functions as func
from mario import Mario
from pygame.sprite import Group


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((980, 224 * 3))
        pygame.display.set_caption("Super Mario")

        self.modx = 0
        self.maxx = 0
        self.solids = Group()
        self.bricks = Group()
        self.level = Level(self.screen, self.solids, self.bricks, self)
        self.mario = Mario(self.screen, self.solids, self.bricks, self)

    def play(self):
        while True:
            pygame.time.Clock().tick(60)
            func.check_events(self.mario)
            self.mario.update()
            self.level.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.level.blitme()
        self.mario.blitme()
        pygame.display.flip()

game = Game()
game.play()