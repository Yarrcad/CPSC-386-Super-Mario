import pygame
from pygame.sprite import Sprite
import spritesheet


class Mario(Sprite):

    def __init__(self, screen, solids, bricks):
        super().__init__()
        self.screen = screen
        self.solids = solids
        self.bricks = bricks
<<<<<<< HEAD
        self.game = game
<<<<<<< HEAD
        self.temp = Group()
        self.temp.add(self)
=======
>>>>>>> origin/master
=======
>>>>>>> parent of a408614... update

        ss = spritesheet.spritesheet('images/mario.png')
        self.rimages = ss.images_at(((97, 1, 15, 31), (114, 1, 15, 31), (131, 1, 16, 31)), colorkey=(146, 39, 143))

<<<<<<< HEAD
        # Mario
        self.rimages = ss.images_at(((97, 33, 17, 17), (114, 33, 17, 17), (131, 33, 16, 17)), colorkey=(146, 39, 143))
        self.simage = ss.image_at((79, 33, 17, 17), colorkey=(146, 39, 143))
        self.dimage = ss.image_at((181, 33, 17, 17), colorkey=(146, 39, 143))
        self.jimage = ss.image_at((164, 33, 17, 17), colorkey=(146, 39, 143))

        # Fire Mario
        self.frimages = ss.images_at(((97, 128, 17, 31), (114, 128, 17, 31), (131, 128, 16, 31)), colorkey=(146, 39, 143))
        self.fsimage = ss.image_at((79, 128, 17, 31), colorkey=(146, 39, 143))
        self.fdimage = ss.image_at((181, 128, 17, 31), colorkey=(146, 39, 143))
        self.fjimage = ss.image_at((164, 128, 17, 31), colorkey=(146, 39, 143))

<<<<<<< HEAD
        self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
=======
        self.image = pygame.transform.scale(self.rimages[0], (15 * 3, 31 * 3))
>>>>>>> origin/master
=======
        self.image = pygame.transform.scale(self.simage, (17 * 3, 31 * 3))
>>>>>>> parent of a408614... update
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.ducking = False
        self.grounded = True
        self.index = 0
<<<<<<< HEAD
<<<<<<< HEAD
        self.speed = 4
=======
        self.speed = 8
        self.xspeed = 8
>>>>>>> origin/master
=======
        self.speed = 8
>>>>>>> parent of a408614... update
        self.xvelo = 0
        self.yvelo = 0
        self.xp = False
        self.jumping = False
        self.recent = None
<<<<<<< HEAD
=======
        self.fire = True
        self.norm = False
        self.superMario = False
        self.boosted = False
        self.pressed = False
        self.recent = None
        self.maxs = 5
        self.xvelot = 4
>>>>>>> parent of a408614... update

    def update(self):
<<<<<<< HEAD
        if self.ducking and self.norm and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.dimage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 8
        elif self.ducking and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.dimage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.norm and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.jimage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.jimage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.norm and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.simage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo > 0 and self.norm:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.rimages):
                    self.index = 0
                self.image = pygame.transform.scale(self.rimages[self.index], (17 * 3, 17 * 3))
                self.speed = 8
        elif self.xvelo < 0 and self.norm:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.rimages):
                    self.index = 0
                self.image = pygame.transform.flip(pygame.transform.scale(self.rimages[self.index], (17 * 3, 17 * 3)), True, False)
                self.speed = 8
        
        if self.ducking and self.superMario and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.sdimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif self.ducking and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.sdimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.superMario and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.sjimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.sjimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.superMario and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.ssimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.ssimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo > 0 and self.superMario:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.srimages):
                    self.index = 0
                self.image = pygame.transform.scale(self.srimages[self.index], (17 * 3, 31 * 3))
                self.speed = 8
        elif self.xvelo < 0 and self.superMario:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.srimages):
                    self.index = 0
                self.image = pygame.transform.flip(pygame.transform.scale(self.srimages[self.index], (17 * 3, 31 * 3)), True, False)
                self.speed = 8
                
        if self.ducking and self.fire and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fdimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif self.ducking and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fdimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.fire  and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fjimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif not self.grounded and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fjimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.fire and (self.recent == None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fsimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 8
        elif self.xvelo == 0 and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fsimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 8
        elif self.xvelo > 0 and self.fire:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.frimages):
                    self.index = 0
                self.image = pygame.transform.scale(self.frimages[self.index], (17 * 3, 31 * 3))
                self.speed = 8
        elif self.xvelo < 0 and self.fire:
            self.speed -= 1
            if self.speed <= 0:
                self.index += 1
                if self.index == len(self.frimages):
                    self.index = 0
                self.image = pygame.transform.flip(pygame.transform.scale(self.frimages[self.index], (17 * 3, 31 * 3)), True, False)
                self.speed = 8

        if self.rect.centerx < 490 or self.xvelo < 0:
            self.rect.centerx += self.xvelo
<<<<<<< HEAD
=======
        self.speed -= 1
        if self.speed == 0:
            self.index += 1
            if self.index == len(self.rimages):
                self.index = 0
            self.image = pygame.transform.scale(self.rimages[self.index], (15 * 3, 31 * 3))
            self.speed = 8
        self.rect.centerx += self.xvelo
>>>>>>> origin/master
=======
        else:
            self.game.modx = self.xvelo
>>>>>>> parent of a408614... update
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if solid.rect.left >= self.rect.right:
                self.rect.right = solid.rect.left - 1
                self.xvelo = 0
            if solid.rect.right <= self.rect.left:
                self.rect.left = solid.rect.right + 1
                self.xvelo = 0
        self.rect.centery -= self.yvelo
        if self.yvelo >= 19:
            self.jumping = False
        if not self.jumping:
            self.yvelo -= 2
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
<<<<<<< HEAD:SuperMario1-1 - Copy/mario.py
            if self.rect.centerx > solid.rect.right and self.rect.bottom < solid.rect.top:
                self.rect.left = solid.rect.right + 1
            elif self.rect.centerx < solid.rect.left and self.rect.bottom < solid.rect.top:
                self.rect.right = solid.rect.left - 1
            elif self.rect.centery > solid.rect.centery:
=======
            if solid.rect.bottom <= self.rect.top:
>>>>>>> d91a8e5aed99c79f76a09506118f8fcc28fe1b63:SuperMario1-1/mario.py
                self.rect.top = solid.rect.bottom + 1
                self.yvelo = 0
            elif solid.rect.top <= self.rect.bottom:
                self.rect.bottom = solid.rect.top - 1
                self.grounded = True
                self.speed = 0
                self.yvelo = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.xvelo = 0
<<<<<<< HEAD
        if (not self.pressed and self.xvelo > 0 or self.xvelo > self.maxs) and self.grounded:
            self.xvelot -= 1
            if self.xvelot == 0:
                self.xvelo -= 1
                self.xvelot = 2
        elif (not self.pressed and self.xvelo < 0 or self.xvelo < self.maxs * -1) and self.grounded:
            self.xvelot -= 1
            if self.xvelot == 0:
                self.xvelo += 1
                self.xvelot = 2
        else:
            self.xvelot = 4
        if self.rect.centerx >= 490 and self.xvelo > 0:
            self.game.modx = self.xvelo
        else:
            self.game.modx = 0
=======
        if not self.xp:
            self.xspeed -= 1
            if self.xspeed == 0:
                if self.xvelo > 0:
                    self.xvelo -= 2
                elif self.xvelo < 0:
                    self.xvelo += 2
                self.xspeed = 8
>>>>>>> origin/master

    def blitme(self):
        self.screen.blit(self.image, self.rect)
