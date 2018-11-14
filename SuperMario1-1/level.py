import pygame
from grouper import Grouper
from brick import Brick
from goomba import Goomba
from koopa import Koopa


class Level:

    def __init__(self, screen, solids, bricks, game, scoreboard, coins, muushrooms, fflowers, goombas, koopas, fireballs, audio):
        self.fireballs = fireballs
        self.coins = coins
        self.mushrooms = muushrooms
        self.audio = audio
        self.fflowers = fflowers
        self.screen = screen
        self.grouper = Grouper
        self.scoreboard = scoreboard
        self.brick = Brick
        self.game = game
        self.bricks = bricks
        self.background = pygame.image.load('images/background.png')
        self.rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (self.rect.right * 3, self.rect.bottom * 3))
        self.rect = self.background.get_rect()
        self.solids = solids
        self.koopa = Koopa
        self.koopas = koopas
        self.goomba = Goomba
        self.goombas = goombas
        # Ground
        self.solids.add(self.grouper(0 * 3, 200 * 3, 1103 * 3, 22 * 3))
        self.solids.add(self.grouper(1136 * 3, 200 * 3, 239 * 3, 22 * 3))
        self.solids.add(self.grouper(1424 * 3, 200 * 3, 1023 * 3, 22 * 3))
        self.solids.add(self.grouper(2480 * 3, 200 * 3, 911 * 3, 22 * 3))
        # Small pipe
        self.solids.add(self.grouper(448 * 3, 168 * 3, 31 * 3, 32 * 3))
        self.solids.add(self.grouper(2608 * 3, 168 * 3, 31 * 3, 32 * 3))
        self.solids.add(self.grouper(2864 * 3, 168 * 3, 31 * 3, 32 * 3))
        # Med Pipe
        self.solids.add(self.grouper(608 * 3, 152 * 3, 31 * 3, 48 * 3))
        # Large Pipe
        self.solids.add(self.grouper(736 * 3, 136 * 3, 31 * 3, 64 * 3))
        self.solids.add(self.grouper(912 * 3, 136 * 3, 31 * 3, 64 * 3))
        # Solid Bricks
        self.solids.add(self.grouper(2144 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 1) * 3, (184 - 16 * 1) * 3, (63 - 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 2) * 3, (184 - 16 * 2) * 3, (63 - 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper((2144 + 16 * 3) * 3, (184 - 16 * 3) * 3, (63 - 16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 1) * 3, (16 + 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 2) * 3, (16 + 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper(2240 * 3, (184 - 16 * 3) * 3, (16 + 16 * 0) * 3, 64 * 3))
        self.solids.add(self.grouper(2368 * 3, 184 * 3, 79 * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 1) * 3, (184 - 16 * 1) * 3, (79 - 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 2) * 3, (184 - 16 * 2) * 3, (79 - 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper((2368 + 16 * 3) * 3, (184 - 16 * 3) * 3, (79 - 16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, 184 * 3, 63 * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 1) * 3, (16 + 16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 2) * 3, (16 + 16 * 1) * 3, 64 * 3))
        self.solids.add(self.grouper(2480 * 3, (184 - 16 * 3) * 3, (16 + 16 * 0) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 0) * 3, (184 - 16 * 0) * 3, (16 * 9) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 1) * 3, (184 - 16 * 1) * 3, (16 * 8) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 2) * 3, (184 - 16 * 2) * 3, (16 * 7) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 3) * 3, (184 - 16 * 3) * 3, (16 * 6) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 4) * 3, (184 - 16 * 4) * 3, (16 * 5) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 5) * 3, (184 - 16 * 5) * 3, (16 * 4) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 6) * 3, (184 - 16 * 6) * 3, (16 * 3) * 3, 64 * 3))
        self.solids.add(self.grouper((2896 + 16 * 7) * 3, (184 - 16 * 7) * 3, (16 * 2) * 3, 64 * 3))
        self.solids.add(self.grouper(3168 * 3, 184 * 3, 16 * 3, 16 * 3))
        # Regular Bricks
        self.bricks.add(self.brick(1280 * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 1) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 2) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 3) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 4) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 5) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 6) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 7) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 11) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 12) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 13) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick(1936 * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 1) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 2) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 7) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 10) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick(320 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(352 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(384 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1232 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1264 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1504 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1560 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1576 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1888 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2064 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2079 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2688 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2704 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2736 * 3, 136 * 3, 1, self.screen))
        # Question Bricks
        self.bricks.add(self.brick(352 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(1504 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(1744 * 3, 72 * 3, 5, self.screen))
        self.bricks.add(self.brick(2064 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(2080 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(256 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(336 * 3, 136 * 3, 5, self.screen))
        self.bricks.add(self.brick(368 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1248 * 3, 136 * 3, 5, self.screen))
        self.bricks.add(self.brick(1696 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1744 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1792 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(2720 * 3, 136 * 3, 3, self.screen))
        self.goombas.add(self.goomba(self.screen, 352, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 640, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 816, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 839, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1280, 79, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1312, 79, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1553, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1576, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1824, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1847, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1984, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2007, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2084, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2071, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2784, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2807, 200, self.solids, self.bricks))

    def blitme(self):
        self.screen.blit(self.background, self.rect)
        self.coins.draw(self.screen)
        self.mushrooms.draw(self.screen)
        self.fflowers.draw(self.screen)
        for brick in self.bricks:
            brick.blit()
        self.bricks.draw(self.screen)
        self.koopas.draw(self.screen)
        for goomba in self.goombas:
            goomba.blit()


    def update(self):
        self.solids.update(self.game.modx)
        self.rect.centerx -= self.game.modx
        self.bricks.update(self.game.modx)
        self.coins.update(self.game.modx)
        self.mushrooms.update(self.game.modx)
        self.fflowers.update(self.game.modx)
        self.goombas.update(self.game.modx, self.game.maxx)
        self.koopas.update(self.game.modx, self.game.maxx)
        if pygame.sprite.groupcollide(self.fireballs, self.goombas, True, True):
            self.audio.effects.play(self.audio.jumpkill)

    def populateenemies(self):
        #  Enemies
        self.bricks.empty()
        # Regular Bricks
        self.bricks.add(self.brick(1280 * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 1) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 2) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 3) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 4) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 5) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 6) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 7) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 11) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 12) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1280 + 16 * 13) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick(1936 * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 1) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 2) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 7) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick((1936 + 16 * 10) * 3, 72 * 3, 1, self.screen))
        self.bricks.add(self.brick(320 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(352 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(384 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1232 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1264 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1504 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1560 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1576 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(1888 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2064 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2079 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2688 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2704 * 3, 136 * 3, 1, self.screen))
        self.bricks.add(self.brick(2736 * 3, 136 * 3, 1, self.screen))
        # Question Bricks
        self.bricks.add(self.brick(352 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(1504 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(1744 * 3, 72 * 3, 5, self.screen))
        self.bricks.add(self.brick(2064 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(2080 * 3, 72 * 3, 3, self.screen))
        self.bricks.add(self.brick(256 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(336 * 3, 136 * 3, 5, self.screen))
        self.bricks.add(self.brick(368 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1248 * 3, 136 * 3, 5, self.screen))
        self.bricks.add(self.brick(1696 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1744 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(1792 * 3, 136 * 3, 3, self.screen))
        self.bricks.add(self.brick(2720 * 3, 136 * 3, 3, self.screen))
        self.koopas.empty()
        self.goombas.empty()
        self.goombas.add(self.goomba(self.screen, 352, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 640, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 816, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 839, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1280, 79, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1312, 79, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1553, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1576, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1824, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1847, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 1984, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2007, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2084, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2071, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2784, 200, self.solids, self.bricks))
        self.goombas.add(self.goomba(self.screen, 2807, 200, self.solids, self.bricks))
