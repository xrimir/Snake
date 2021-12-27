from Classes.Game import Game
from Classes.Menu.StartMenu import StartMenu
from Classes.Menu.GameOverMenu import GameOverMenu

game = Game()
start_menu = StartMenu(game)
game_over_menu = GameOverMenu(game)

while game.running:
    start_menu.display_menu()
    game.start_game()
    game_over_menu.display_menu()
