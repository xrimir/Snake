from Classes.Game import Game


class Menu:
    def __init__(self, game):
        self.game = Game()
        self.screen = self.game.screen
        self.clock = self.game.clock
        self.state = True
