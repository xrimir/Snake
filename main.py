import sys
from Classes.Snake import Snake
from Classes.Fruit import Fruit
import pygame
import time

pygame.init()
pygame.font.init()
SIZE = WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

class Game:
    score = 0
    game_status = True

    def score_point(self):
        self.score += 1

    def render_text(self, window):
        font = pygame.font.SysFont("Arial", 25)
        text = f"Score: {self.score}"
        x = font.render(text, False, (255, 255, 255))
        window.blit(x, (1, 1))

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
    fruit.draw_fruit(screen)
    snake.move_tail(screen)
    snake.draw_snake(screen)
    if snake.check_fruit_collision(fruit.x, fruit.y):
        fruit.refresh_fruit()
        game.score_point()
        snake.snake_grow()
    game.render_text(screen)
    pygame.display.update()
    clock.tick(60)
