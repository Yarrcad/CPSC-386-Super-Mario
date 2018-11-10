import pygame
from level import Level
import functions as func
from mario import Mario
from pygame.sprite import Group


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((980, 224 * 3))
        pygame.display.set_caption("Super Mario")

<<<<<<< HEAD
        self.modx = 0
        self.maxx = 0
=======
>>>>>>> origin/master
        self.solids = Group()
        self.bricks = Group()
        self.level = Level(self.screen, self.solids, self.bricks)
        self.mario = Mario(self.screen, self.solids, self.bricks)

    def play(self):
        while True:
            pygame.time.Clock().tick(60)
            func.check_events(self.mario)
            self.mario.update()
            self.update_screen()

    def update_screen(self):
        self.level.blitme()
        self.mario.blitme()
        pygame.display.flip()

game = Game()
game.play()