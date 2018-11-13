import pygame
from level import Level
import functions as func
from mario import Mario
from scoreboard import Scoreboard
from startup_menu import Startup
from pygame.sprite import Group



class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((980, 224 * 3))
        pygame.display.set_caption("Super Mario")

        self.modx = 0
        self.maxx = 0
        self.fireballs = Group()
        self.coins = Group()
        self.mushrooms = Group()
        self.fflowers = Group()
        self.solids = Group()
        self.bricks = Group()
        self.startup=Startup(self.screen)
        self.scoreboard = Scoreboard(self.screen)
        self.level = Level(self.screen, self.solids, self.bricks, self, self.scoreboard, self.coins, self.mushrooms, self.fflowers)
        self.mario = Mario(self.screen, self.solids, self.bricks, self, self.scoreboard, self.coins, self.mushrooms, self.fflowers)
        pygame.mixer.music.load('sounds/maintheme.mp3')
        pygame.mixer.music.play(-1)
    def play(self):
        while True:

            pygame.time.Clock().tick(60)
            func.check_events(self.mario,self.startup,self.scoreboard)
            self.update_screen()
            if not self.startup.menu_active:
                self.mario.update()
                self.level.update()

                self.fireballs.update(self.modx)
                for fireball in self.fireballs:
                    if not fireball.active:
                        self.fireballs.remove(fireball)
                        self.mario.fcount -= 1
                for brick in self.bricks:
                    if not brick.active:
                        self.bricks.remove(brick)
                for coin in self.coins:
                    if not coin.active:
                        self.coins.remove(coin)
                for fflower in self.fflowers:
                    if not fflower.active:
                        self.fflowers.remove(fflower)
                for mushroom in self.mushrooms:
                    if not mushroom.active:
                        self.mushrooms.remove(mushroom)


    def update_screen(self):
        self.level.blitme()

        #self.screen.fill(Game.BLACK)

        self.mario.blitme()
        self.fireballs.draw(self.screen)
        self.scoreboard.blit()
        if self.startup.menu_active:
            self.startup.blit()
        pygame.display.flip()

game = Game()
game.play()