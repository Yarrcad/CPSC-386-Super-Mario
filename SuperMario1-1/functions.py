import pygame
import sys


def check_keydown_events(event, mario):
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        mario.ducking = True

def check_keyup_events(event, mario):
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        mario.ducking = False


def check_events(mario):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if mario.xvelo <= 5:
            mario.xvelo += 1
        mario.xp = True
        mario.recent = 'right'
    else:
        mario.xp = False
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if mario.xvelo >= -5:
            mario.xvelo -= 1
            mario.xp = True
        mario.recent = 'left'
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if mario.grounded and not mario.jumping:
            mario.jumping = True
            mario.grounded = False
        if mario.jumping:
            if mario.yvelo <= 19:
                mario.yvelo += 2
    else:
        mario.jumping = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.key.get_pressed():
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keydown_events(event, mario)
