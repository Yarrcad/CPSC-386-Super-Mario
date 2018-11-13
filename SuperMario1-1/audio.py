import pygame


class Audio:
    def __init__(self):
        # Create mixer for audio.
        pygame.mixer.init()
        pygame.mixer.set_num_channels(1)
        self.effects = pygame.mixer.Channel(0)
        self.up = pygame.mixer.Sound("sounds/1-up.wav")
        self.bsmash = pygame.mixer.Sound("sounds/bricksmash.wav")
        self.coin = pygame.mixer.Sound("sounds/coin.wav")
        self.enemyk = pygame.mixer.Sound("sounds/enemykill.wav")
        self.fireball = pygame.mixer.Sound("sounds/fireball.wav")
        self.itemapp = pygame.mixer.Sound("sounds/item_appears.wav")
        self.jumpkill = pygame.mixer.Sound("sounds/jumpkill.wav")
        self.piptrav = pygame.mixer.Sound("sounds/pipe_travel.wav")
        self.powerup = pygame.mixer.Sound("sounds/power_up.wav")
        self.jump = pygame.mixer.Sound("sounds/jump.wav")


    @staticmethod
    def play():
        # Play background music.
        pygame.mixer.music.load("sounds/maintheme.mp3")
        pygame.mixer_music.set_volume(.5)
        pygame.mixer.music.play()
