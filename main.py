import sys

import pygame

pygame.font.init()
from Classes.Snake import Snake
from Classes.Fruit import Fruit
from Classes.UI.Button import Btn
from Classes.UI.Text import Text
import random
import time

pygame.init()
SIZE = WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")


class Game:
    score = 0
    game_status = True
    font_arial = pygame.font.SysFont("Arial", 25)

    def score_point(self):
        self.score += 1

    def render_text(self, text, window, x, y, align_center=False):
        text_render = self.font_arial.render(text, True, (255, 255, 255))
        if align_center:
            window.blit(text_render, (x - text_render.get_size()[0] // 2, y - text_render.get_size()[1] // 2))
        else:
            window.blit(text_render, (x, y))

    def draw_grid(self, window):
        grid_lines = 20
        grid_width = WIDTH // grid_lines
        x = 0
        y = 0
        for num in range(grid_lines):
            x += grid_width
            y += grid_width
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, WIDTH))
            pygame.draw.line(window, (255, 255, 255), (0, y), (HEIGHT, y))

    def game_over(self, snake):
        if snake.y < 0:
            self.game_status = False
        elif snake.x < 0:
            self.game_status = False
        elif (snake.y + snake.VELOCITY) + snake.SNAKE_HEIGHT // 2 > HEIGHT:
            self.game_status = False
        elif (snake.x + snake.VELOCITY) + snake.SNAKE_WIDTH // 2 > WIDTH:
            self.game_status = False


game = Game()


def start_game():
    snake = Snake()
    fruit = Fruit()
    while game.game_status:
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            snake.set_direction(event)
        for node in snake.snake_body:
            node["pos"] = (node["x"], node["y"])
        snake.move_snake()
        game.game_over(snake)
        for num in range(1, len(snake.snake_body)):
            if snake.x == snake.snake_body[num]["x"] and snake.y == snake.snake_body[num]["y"]:
                game.game_status = False
        screen.fill((0, 0, 0))
        game.draw_grid(screen)
        game.render_text(f"Score: {game.score}", screen, 1, 1)
        fruit.draw_fruit(screen)
        snake.move_tail(screen)
        snake.draw_snake(screen)
        if snake.check_fruit_collision(fruit.x, fruit.y):
            fruit.refresh_fruit()
            game.score_point()
            snake.snake_grow()
        pygame.display.update()
        clock.tick(30)


def game_over_menu():
    game_over_btn = Btn(500 - 100, 500 - 25, 200, 50, (255, 0, 0), screen)
    game_over_text = Text("GAME OVER", 500, 500, screen, True)
    start_over_btn = Btn(500 - 100, 600 - 25, 200, 50, (104, 124, 156), screen)
    start_over_text = Text("START OVER", 500, 600, screen, True)
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_over_btn.check_for_collision(mx, my):
                        print("START OVER")
                    if game_over_btn.check_for_collision(mx, my):
                        print("GAME OVER")

        screen.fill((0, 0, 0))
        game_over_btn.draw_button()
        game_over_text.draw_text()
        start_over_btn.draw_button()
        start_over_text.draw_text()

        pygame.display.update()
        clock.tick(30)


start_game()
game_over_menu()
