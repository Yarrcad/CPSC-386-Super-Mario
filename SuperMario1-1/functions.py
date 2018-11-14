import pygame
import sys
from fireball import Fireball


def check_keydown_events(event, mario, audio):
    if event.key == pygame.K_s and not mario.norm:
        mario.ducking = True
    if event.key == pygame.K_d:
        mario.recent = 'd'
    if event.key == pygame.K_a:
        mario.recent = 'a'
    if event.key == pygame.K_w and mario.grounded and not mario.jumping:
        mario.jumping = True
        mario.grounded = False
        audio.effects.play(audio.jump)
    if event.key == pygame.K_SPACE and mario.fire:
        mario.game.fireballs.add(Fireball(mario, mario.solids, mario.bricks))
        audio.effects.play(audio.fireball)


def check_keyup_events(event, mario):
    if event.key == pygame.K_s and not mario.norm:
        mario.ducking = False


def check_events(mario, audio, startup):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario, audio)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_for_play(startup, mouse_x, mouse_y)
            check_for_hs(startup, mouse_x, mouse_y)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        mario.maxs = 10
    else:
        mario.maxs = 5
    if keys[pygame.K_d] and mario.recent == 'd' and not mario.ducking:
        if mario.xvelo <= mario.maxs:
            mario.xvelo += 1
        mario.pressed = True
    elif keys[pygame.K_a] and mario.recent == 'a' and not mario.ducking:
        if mario.xvelo >= mario.maxs * -1:
            mario.xvelo -= 1
        mario.pressed = True
    else:
        mario.pressed = False
    if keys[pygame.K_w] and mario.jumping:
        if mario.yvelo <= 19:
            mario.yvelo += 2
    else:
        mario.jumping = False


def check_for_play(startup, mouse_x, mouse_y):
    button_clicked = startup.playrect.collidepoint(mouse_x, mouse_y)
    if button_clicked and startup.menu_active:
        startup.menu_active = False

def check_for_hs(startup, mouse_x, mouse_y):
    button_clicked = startup.score_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and startup.menu_active and not startup.hs_active:
        startup.hs_active = True
    elif button_clicked and startup.menu_active and startup.hs_active:
        startup.hs_active = False
