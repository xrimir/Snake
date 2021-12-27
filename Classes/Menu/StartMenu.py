import sys

import pygame

from Classes.UI.Button import Button
from Classes.UI.Text import Text
from Classes.Menu.Menu import Menu


class StartMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        start_btn = Button(500 - 100, 500 - 25, 200, 50, (104, 124, 156), self.screen)
        start_text = Text("Play", 500, 500, self.screen, True)
        options_btn = Button(500 - 100, 600 - 25, 200, 50, (255, 0, 0), self.screen)
        options_text = Text("Options", 500, 600, self.screen, True)

        bg = pygame.image.load("./static/matrix.jpg")
        pygame.mixer.music.load("./static/matrix_theme.wav")
        pygame.mixer.music.play(-1)
        while True:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if start_btn.check_for_collision(mx, my):
                            return 0
                        if options_btn.check_for_collision(mx, my):
                            sys.exit(0)

            self.screen.fill((0, 0, 0))
            self.screen.blit(bg, (500 - bg.get_size()[0] // 2, 500 - bg.get_size()[1] // 2))
            start_btn.draw_button()
            start_text.draw_text()
            options_btn.draw_button()
            options_text.draw_text()
            pygame.display.update()
            self.clock.tick(30)
