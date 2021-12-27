import sys

import pygame


from Classes.UI.Button import Button
from Classes.UI.Text import Text
from Classes.Menu.Menu import Menu


class GameOverMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        game_over_btn = Button(500 - 100, 500 - 25, 200, 50, (104, 124, 156), self.screen)
        game_over_text = Text("GIVE UP", 500, 500, self.screen, True)
        start_over_btn = Button(500 - 100, 600 - 25, 200, 50, (255, 0, 0), self.screen)
        start_over_text = Text("START OVER", 500, 600, self.screen, True)
        bg = pygame.image.load("./static/redpillbluepill.jpeg")
        while True:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if start_over_btn.check_for_collision(mx, my):
                            self.state = False
                            return 0
                        if game_over_btn.check_for_collision(mx, my):
                            sys.exit(0)

            self.screen.fill((0, 0, 0))
            self.screen.blit(bg, (500 - bg.get_size()[0] // 2, 500 - bg.get_size()[1] // 2))
            game_over_btn.draw_button()
            game_over_text.draw_text()
            start_over_btn.draw_button()
            start_over_text.draw_text()
            pygame.display.update()
            self.clock.tick(30)
