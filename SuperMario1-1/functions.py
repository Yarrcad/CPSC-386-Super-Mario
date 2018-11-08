import pygame
import sys


def check_keydown_events(event, mario):
    if event.key == pygame.K_s and not mario.norm:
        mario.ducking = True
    if event.key == pygame.K_d:
        mario.recent = 'd'
    if event.key == pygame.K_a:
        mario.recent = 'a'
    if event.key == pygame.K_w and mario.grounded and not mario.jumping:
        mario.jumping = True
        mario.grounded = False

def check_keyup_events(event, mario):
    if event.key == pygame.K_s and not mario.norm:
        mario.ducking = False


def check_events(mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)
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

