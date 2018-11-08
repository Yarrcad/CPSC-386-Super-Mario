import pygame
from grouper import Grouper
from brick import Brick



class Level:

    def __init__(self, screen, solids, bricks, game):
        self.screen = screen
        self.grouper = Grouper
        self.brick = Brick
        self.game = game
        self.bricks = bricks
        self.background = pygame.image.load('images/background.png')
        self.rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (self.rect.right * 3, self.rect.bottom * 3))
        self.rect = self.background.get_rect()
        self.solids = solids
        # Ground
        self.solids.add(self.grouper(0 * 3, 200 * 3, 1103 * 3, 22 * 3))
        self.solids.add(self.grouper(1136 * 3, 200 * 3, 239 * 3, 22 * 3))
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
        # Regular Bricks
        self.bricks.add(self.brick(320 * 3, 144 * 3, 1))
        self.bricks.add(self.brick(352 * 3, 144 * 3, 1))
        self.bricks.add(self.brick(384 * 3, 144 * 3, 1))

    def blitme(self):
        self.screen.blit(self.background, self.rect)
        self.bricks.draw(self.screen)

    def update(self):
        self.solids.update(self.game.modx)
        self.rect.centerx -= self.game.modx
        self.bricks.update(self.game.modx)
