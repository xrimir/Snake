import pygame
from Classes.Snake import Snake
from Classes.Fruit import Fruit
from Classes.UI.Button import Button
from Classes.UI.Text import Text
import time
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 2000, 1000
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.score = 0
        self.running = True
        self.game_status = False
        self.clock = pygame.time.Clock()
        self.FPS = 10

        pygame.display.set_caption("Snake")

    def score_point(self):
        self.score += 1

    def score_reset(self):
        self.score -= 1

    def draw_grid(self, window):
        grid_lines = 40
        grid_width = self.WIDTH // grid_lines
        x = 0
        y = 0
        for num in range(grid_lines):
            x += grid_width
            y += grid_width
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, self.WIDTH))
            pygame.draw.line(window, (255, 255, 255), (0, y), (self.HEIGHT, y))

    def game_over(self, snake):
        if snake.y < 0:
            self.game_status = False
        elif snake.x < 0:
            self.game_status = False
        elif snake.y == self.HEIGHT:
            self.game_status = False
        elif snake.x == self.WIDTH:
            self.game_status = False

    def start_game(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("./static/ost.wav")
        # pygame.mixer.music.play(-1)
        snake = Snake()
        fruit = Fruit()
        self.game_status = True
        while self.game_status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                snake.set_direction(event)
            for node in snake.snake_body:
                node["pos"] = (node["x"], node["y"])
            if not snake.direction_flag:
                snake.move_snake()
            snake.direction_flag = False
            self.game_over(snake)

            # Do metody game over / export
            for num in range(2, len(snake.snake_body)):
                if snake.x == snake.snake_body[num]["x"] and snake.y == snake.snake_body[num]["y"]:
                    self.game_status = False
            # rendering to the screen gui
            self.screen.fill((0, 0, 0))
            self.draw_grid(self.screen)
            Text.render_text(f"Score: {self.score}", self.screen, 1, 1)
            fruit.draw_fruit(self.screen)
            snake.move_tail(self.screen)
            snake.draw_snake(self.screen)
            if snake.check_fruit_collision(fruit.x, fruit.y):
                fruit.refresh_fruit()
                self.score_point()
                snake.snake_grow()
            pygame.display.update()
            self.clock.tick(self.FPS)
        pygame.mixer.music.unload()
        self.score_reset()
        del snake
        del fruit
