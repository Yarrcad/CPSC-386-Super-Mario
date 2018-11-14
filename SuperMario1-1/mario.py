import pygame
from pygame.sprite import Sprite
import spritesheet
from pygame.sprite import Group
from coin import Coin
from fflower import Fflower
from mushroom import Mushroom


class Mario(Sprite):

    def __init__(self, screen, solids, bricks, game, scoreboard, coins, muushrooms, fflowers, audio, level, startup):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.coins = coins
        self.audio = audio
        self.flower = Fflower
        self.startup = startup
        self.mushrooms = muushrooms
        self.mushroom = Mushroom
        self.fflowers = fflowers
        self.coin = Coin
        self.solids = solids
        self.scoreboard = scoreboard
        self.bricks = bricks
        self.game = game
        self.invuln = False
        self.invulncounter = 24
        self.temp = Group()
        self.temp.add(self)
        self.level = level

        ss = spritesheet.spritesheet('images/mario.png')
        # Super Mario
        self.srimages = ss.images_at(((97, 1, 17, 31), (114, 1, 17, 31), (131, 1, 16, 31)), colorkey=(146, 39, 143))
        self.ssimage = ss.image_at((79, 1, 17, 31), colorkey=(146, 39, 143))
        self.sdimage = ss.image_at((181, 1, 17, 31), colorkey=(146, 39, 143))
        self.sjimage = ss.image_at((164, 1, 17, 31), colorkey=(146, 39, 143))
        self.stimage = ss.image_at((147, 1, 17, 31), colorkey=(146, 39, 143))

        # Mario
        self.rimages = ss.images_at(((97, 33, 17, 17), (114, 33, 17, 17), (131, 33, 16, 17)), colorkey=(146, 39, 143))
        self.simage = ss.image_at((79, 33, 17, 17), colorkey=(146, 39, 143))
        self.dimage = ss.image_at((181, 33, 17, 17), colorkey=(146, 39, 143))
        self.jimage = ss.image_at((164, 33, 17, 17), colorkey=(146, 39, 143))
        self.timage = ss.image_at((147, 33, 17, 17), colorkey=(146, 39, 143))

        # Fire Mario
        self.frimages = ss.images_at(((97, 128, 17, 31), (114, 128, 17, 31), (131, 128, 16, 31)),
                                     colorkey=(146, 39, 143))
        self.fsimage = ss.image_at((79, 128, 17, 31), colorkey=(146, 39, 143))
        self.fdimage = ss.image_at((181, 128, 17, 31), colorkey=(146, 39, 143))
        self.fjimage = ss.image_at((164, 128, 17, 31), colorkey=(146, 39, 143))
        self.ftimage = ss.image_at((147, 128, 17, 31), colorkey=(146, 39, 143))

        self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.ducking = False
        self.grounded = True
        self.index = 0
        self.speed = 4
        self.xvelo = 0
        self.yvelo = 0
        self.jumping = False
        self.recent = None
        self.fire = False
        self.norm = True
        self.superMario = False
        self.boosted = False
        self.pressed = False
        self.recent = None
        self.maxs = 5
        self.xvelot = 4
        self.fcount = 0
        self.dead = False

    def update(self):
        if self.invuln:
            self.invulncounter -= 1
            if self.invulncounter <= 0:
                self.invulncounter = 24
                self.invuln = False
        if self.ducking and self.norm and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.dimage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 4
        elif self.ducking and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.dimage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.norm and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.jimage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.jimage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.norm and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.norm and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.simage, (17 * 3, 17 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo > 0 and self.norm:
            if self.recent == 'a':
                self.image = pygame.transform.flip(pygame.transform.scale(self.timage, (17 * 3, 17 * 3)), True, False)
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.rimages):
                        self.index = 0
                    self.image = pygame.transform.scale(self.rimages[self.index], (17 * 3, 17 * 3))
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4
        elif self.xvelo < 0 and self.norm:
            if self.recent == 'd':
                self.image = pygame.transform.scale(self.timage, (17 * 3, 17 * 3))
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.rimages):
                        self.index = 0
                    self.image = pygame.transform.flip(
                        pygame.transform.scale(self.rimages[self.index], (17 * 3, 17 * 3)), True, False)
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4

        if self.ducking and self.superMario and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.sdimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif self.ducking and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.sdimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.superMario and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.sjimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.sjimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.superMario and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.ssimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.superMario and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.ssimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo > 0 and self.superMario:
            if self.recent == 'a':
                self.image = pygame.transform.flip(pygame.transform.scale(self.stimage, (17 * 3, 31 * 3)), True, False)
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.srimages):
                        self.index = 0
                    self.image = pygame.transform.scale(self.srimages[self.index], (17 * 3, 31 * 3))
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4
        elif self.xvelo < 0 and self.superMario:
            if self.recent == 'd':
                self.image = pygame.transform.scale(self.stimage, (17 * 3, 31 * 3))
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.srimages):
                        self.index = 0
                    self.image = pygame.transform.flip(
                        pygame.transform.scale(self.srimages[self.index], (17 * 3, 31 * 3)), True, False)
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4

        if self.ducking and self.fire and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fdimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif self.ducking and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fdimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.fire and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fjimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif not self.grounded and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fjimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.fire and (self.recent is None or self.recent == 'd'):
            self.image = pygame.transform.scale(self.fsimage, (17 * 3, 31 * 3))
            self.index = 0
            self.speed = 4
        elif self.xvelo == 0 and self.fire and self.recent == 'a':
            self.image = pygame.transform.flip(pygame.transform.scale(self.fsimage, (17 * 3, 31 * 3)), True, False)
            self.index = 0
            self.speed = 4
        elif self.xvelo > 0 and self.fire:
            if self.recent == 'a':
                self.image = pygame.transform.flip(pygame.transform.scale(self.ftimage, (17 * 3, 31 * 3)), True, False)
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.frimages):
                        self.index = 0
                    self.image = pygame.transform.scale(self.frimages[self.index], (17 * 3, 31 * 3))
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4
        elif self.xvelo < 0 and self.fire:
            if self.recent == 'd':
                self.image = pygame.transform.scale(self.ftimage, (17 * 3, 31 * 3))
            else:
                self.speed -= 1
                if self.speed <= 0:
                    self.index += 1
                    if self.index == len(self.frimages):
                        self.index = 0
                    self.image = pygame.transform.flip(
                        pygame.transform.scale(self.frimages[self.index], (17 * 3, 31 * 3)), True, False)
                    if self.xvelo > 6 or self.xvelo < -6:
                        self.speed = 2
                    else:
                        self.speed = 4
        if self.game.maxx >= 3391 * 3 - 980:
            self.rect.centerx += self.xvelo
        elif self.rect.centerx < 490 or self.xvelo < 0:
            self.rect.centerx += self.xvelo
        goomba = pygame.sprite.spritecollideany(self, self.level.goombas)
        if goomba and not goomba.squish and self.norm:
            self.dead = True
        elif goomba and not goomba.squish:
            self.norm = True
            self.fire = False
            self.superMario = False
            self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
            x = self.rect.centerx
            y = self.rect.centery
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            self.invuln = True
            self.audio.effects.play(self.audio.piptrav)
        koopa =  pygame.sprite.spritecollideany(self, self.level.koopas)
        if koopa and not koopa.squish and self.norm:
            self.dead = True
        elif koopa and not koopa.squish:
            self.norm = True
            self.fire = False
            self.superMario = False
            self.image = pygame.transform.scale(self.simage, (17 * 3, 17 * 3))
            x = self.rect.centerx
            y = self.rect.centery
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            self.invuln = True
            self.audio.effects.play(self.audio.piptrav)
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if self.rect.centerx < solid.rect.centerx:
                self.rect.right = solid.rect.left - 1
                self.xvelo = 0
            if self.rect.centerx > solid.rect.centerx:
                self.rect.left = solid.rect.right + 1
                self.xvelo = 0
        brick = pygame.sprite.spritecollideany(self, self.bricks)
        if brick:
            if self.rect.centerx < brick.rect.centerx:
                self.rect.right = brick.rect.left - 1
                self.xvelo = 0
            if self.rect.centerx > brick.rect.centerx:
                self.rect.left = brick.rect.right + 1
                self.xvelo = 0
        if not self.jumping:
            self.yvelo -= 2
        self.rect.centery -= self.yvelo
        if self.yvelo >= 19:
            self.jumping = False
        solid = pygame.sprite.spritecollideany(self, self.solids)
        if solid:
            if self.jumping:
                self.jumping = False
            if self.rect.centery > solid.rect.centery:
                self.rect.top = solid.rect.bottom + 1
                self.yvelo = 0
            elif self.rect.centery < solid.rect.centery:
                self.rect.bottom = solid.rect.top - 1
                self.grounded = True
                self.yvelo = 0
        else:
            self.grounded = False
        tbricks = pygame.sprite.groupcollide(self.bricks, self.temp, False, False)
        brick = pygame.sprite.spritecollideany(self, self.bricks)
        if brick:
            if self.jumping:
                self.jumping = False
            if self.rect.centery > brick.rect.centery:
                self.rect.top = brick.rect.bottom + 1
                self.yvelo = 0
            elif self.rect.centery < brick.rect.centery:
                self.rect.bottom = brick.rect.top - 1
                self.grounded = True
                self.yvelo = 0
        if len(tbricks) > 1:
            for tbrick in tbricks:
                if tbrick.active and abs(
                        self.rect.centerx - tbrick.rect.centerx) <= 8 * 3 and self.rect.centery > tbrick.rect.centery:
                    if not self.norm and (tbrick.type == 1 or tbrick.type == 2):
                        tbrick.active = False
                        self.audio.effects.play(self.audio.bsmash)
                    elif not tbrick.spent:
                        if tbrick.type == 3:
                            self.coins.add(self.coin(tbrick, 2))
                            self.scoreboard.coins += 1
                            self.audio.effects.play(self.audio.coin)
                            self.scoreboard.score += 200
                            tbrick.spent = True
                        elif tbrick.type == 5 and not self.norm:
                            self.fflowers.add(self.flower(tbrick))
                            self.audio.effects.play(self.audio.itemapp)
                            tbrick.spent = True
                        elif tbrick.type == 5:
                            self.mushrooms.add(self.mushroom(tbrick, self.bricks, self.solids))
                            self.audio.effects.play(self.audio.itemapp)
                            tbrick.spent = True
                    tbrick.bumped = True

        else:
            for tbrick in tbricks:
                if tbrick.active and self.rect.centery > tbrick.rect.centery:
                    tbrick.bumped = True
                    if not self.norm and (tbrick.type == 1 or tbrick.type == 2):
                        tbrick.active = False
                        self.audio.effects.play(self.audio.bsmash)
                        self.scoreboard.score += 50
                    elif not tbrick.spent:
                        if tbrick.type == 3:
                            self.coins.add(self.coin(tbrick, 2))
                            self.scoreboard.coins += 1
                            self.audio.effects.play(self.audio.coin)
                            self.scoreboard.score += 200
                            tbrick.spent = True
                        elif tbrick.type == 5 and not self.norm:
                            self.fflowers.add(self.flower(tbrick))
                            self.audio.effects.play(self.audio.itemapp)
                            tbrick.spent = True
                        elif tbrick.type == 5:
                            self.mushrooms.add(self.mushroom(tbrick, self.bricks, self.solids))
                            self.audio.effects.play(self.audio.itemapp)
                            tbrick.spent = True
        fflower = pygame.sprite.spritecollideany(self, self.fflowers)
        if fflower:
            self.audio.effects.play(self.audio.powerup)
            self.scoreboard.score += 1000
            self.norm = False
            self.superMario = False
            self.fire = True
            fflower.active = False
            self.rect.centery -= 8 * 3
            self.image = pygame.transform.scale(self.simage, (17 * 3, 31 * 3))
            x = self.rect.centerx
            y = self.rect.centery
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        mushroom = pygame.sprite.spritecollideany(self, self.mushrooms)
        if mushroom:
            self.audio.effects.play(self.audio.powerup)
            self.scoreboard.score += 1000
            self.norm = False
            self.superMario = True
            mushroom.active = False
            self.rect.centery -= 8 * 3
            self.image = pygame.transform.scale(self.simage, (17 * 3, 31 * 3))
            x = self.rect.centerx
            y = self.rect.centery
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        goomba = pygame.sprite.spritecollideany(self, self.level.goombas)
        if goomba and self.rect.bottom < goomba.rect.centery and not goomba.squish:
            goomba.squish = True
            goomba.delay = 8
            goomba.rect.centery += 25
            self.yvelo *= -1
            self.audio.effects.play(self.audio.jumpkill)
        koopa = pygame.sprite.spritecollideany(self, self.level.goombas)
        if koopa and self.rect.bottom < koopa.rect.centery:
            goomba.squished = True
            goomba.delay = 8
            self.yvelo *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.xvelo = 0
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
        if self.rect.centerx >= 490 and self.xvelo > 0 and self.game.maxx < 3391 * 3 - 980:
            self.game.modx = self.xvelo
            self.game.maxx += self.xvelo
        elif self.game.maxx > 3391 * 3 - 980:
            self.game.modx = 3391 * 3 - 980 - self.game.maxx
            self.game.maxx = 3391 * 3 - 980
        else:
            self.game.modx = 0
        if self.rect.bottom > 980:  # death from falling into pits
            self.dead = True
        if self.dead and not self. invuln:
            self.die()
        elif self.invuln:
            self.dead = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def die(self):
        self.rect.bottom = 600
        self.rect.left = self.screen_rect.left  # I am having trouble putting mario back to the start
        self.scoreboard.lives -= 1
        self.audio.effects.play(self.audio.death)
        self.game.modx = self.game.maxx * -1 + 12
        self.game.maxx = 0
        self.dead = False
        self.level.populateenemies()
        for brick in self.bricks:
            brick.spent = False
            brick.animate = True
        self.fflowers.empty()
        self.mushrooms.empty()
        if self.scoreboard.lives == 0:
            with open('hs.txt', 'a') as f:
                f.write('\n' + str(self.scoreboard.score))
            self.scoreboard.reset_stats()
            self.startup.menu_active = True
