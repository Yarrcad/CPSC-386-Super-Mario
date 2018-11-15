import pygame
import pygame.font


class Startup:
    def __init__(self, screen, score_button):
        self.screen = screen
        self.menu_active = True
        self.score_button = score_button
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.hs_active = False

        self.title = pygame.image.load_extended('images/title.png')
        self.title = pygame.transform.scale(self.title, (512, 256))
        self.titlerect = self.title.get_rect()

        self.play_button = self.font.render("Play", True, (255, 255, 255))
        self.playrect = self.play_button.get_rect()

        self.titlerect.center = self.screen_rect.center
        self.titlerect.y = 125

        self.playrect.center = self.screen_rect.center
        self.playrect.y = 471
        self.fontb = pygame.font.Font(None, 72)

    def blit(self):
        if not self.hs_active:
            self.screen.blit(self.title, self.titlerect)
            self.screen.blit(self.play_button, self.playrect)
        else:
            fonta = pygame.font.Font(None, 72)
            texta = fonta.render("ALL-TIME", 1, (255, 255, 255))
            widtha, heighta = fonta.size("ALL-TIME")
            recta = pygame.Rect(self.screen.get_width() / 2 - widtha / 2, self.screen.get_height() / 20,
                                widtha, heighta)
            self.screen.blit(texta, recta)
            textb = self.fontb.render("HIGH SCORES:", 1, (255, 255, 255))
            widthb, heightb = self.fontb.size("HIGH SCORES:")
            rectb = pygame.Rect(self.screen.get_width() / 2 - widthb / 2, self.screen.get_height() / 20 +
                                heighta, widthb,
                                heightb)
            self.screen.blit(textb, rectb)
            with open('hs.txt'):
                hscores = [line.rstrip('\n') for line in open('hs.txt')]
                top_scores = []
            for i in range(0, 7):
                max1 = 0
                for j in range(len(hscores)):
                    if int(hscores[j]) > max1:
                        max1 = int(hscores[j])
                hscores.remove(str(max1))
                top_scores.append(max1)
            for i in range(0, 7):
                current_score = top_scores[i]
                font = pygame.font.Font(None, 46)
                text = font.render(str(i + 1) + ". " + str(current_score), 1, (255, 255, 255))
                width, height = font.size(str(i + 1) + ". " + str(current_score))
                rect = pygame.Rect(0, rectb.bottom + 50 * (i + 1), width, height)
                rect.left = rectb.left
                self.screen.blit(text, rect)
        self.score_button.draw_button()
