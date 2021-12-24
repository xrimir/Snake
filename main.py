import sys
import random
import pygame
import time

pygame.init()
pygame.font.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")


def draw_grid(window):
    grid_lines = 20
    grid_width = width // grid_lines
    x = 0
    y = 0
    for num in range(grid_lines):
        x += grid_width
        y += grid_width
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(window, (255, 255, 255), (0, y), (height, y))


class Game:
    score = 0

    def score_point(self):
        self.score += 1

    def render_text(self, window):
        font = pygame.font.SysFont("Arial", 25)
        text = f"Score: {self.score}"
        x = font.render(text, False, (255, 255, 255))
        window.blit(x, (1, 1))


class Snake:
    x = 200
    y = 0

    snake_width = 50
    snake_height = 50
    velocity = 50
    direction = ""
    snake_body = [[50, 0], [100, 0], [150, 0]]

    def make_snake_bigger(self):
        pass
    def update_snake_body(self, window):
        pass

    def set_direction(self, direction):
        self.direction = direction

    def draw_snake(self, window):
        pygame.draw.rect(window, (255, 0, 255), [self.x, self.y, self.snake_width, self.snake_height])


    def check_fruit_collision(self, fruit_x, fruit_y):
        if self.x == fruit_x and self.y == fruit_y:
            return True
        else:
            return False


class Fruit:
    fruit_width = 50
    fruit_height = 50
    fruit_color = (255, 255, 255)
    x = random.randrange(0, width - fruit_width, 50)
    y = random.randrange(0, height - fruit_height, 50)

    def refresh_fruit(self):
        self.x = random.randrange(0, width - self.fruit_width, 50)
        self.y = random.randrange(0, height - self.fruit_height, 50)

    def draw_fruit(self, window):
        pygame.draw.rect(window, self.fruit_color, [self.x, self.y, self.fruit_width, self.fruit_height])


snake = Snake()
fruit = Fruit()
game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != "down":
                snake.set_direction("up")
            if event.key == pygame.K_s and snake.direction != "up":
                snake.set_direction("down")
            if event.key == pygame.K_a and snake.direction != "right":
                snake.set_direction("left")
            if event.key == pygame.K_d and snake.direction != "left":
                snake.set_direction("right")
    if snake.direction == "up" and snake.y > 0:
        snake.y -= snake.velocity
    elif snake.direction == "down" and (snake.y + snake.velocity) + snake.snake_height // 2 < height:
        snake.y += snake.velocity
    elif snake.direction == "left" and snake.x > 0:
        snake.x -= snake.velocity
    elif snake.direction == "right" and (snake.x + snake.velocity) + snake.snake_width // 2 < width:
        snake.x += snake.velocity

    screen.fill((0, 0, 0))
    draw_grid(screen)
    fruit.draw_fruit(screen)
    snake.draw_snake(screen)
    snake.update_snake_body(screen)
    if snake.check_fruit_collision(fruit.x, fruit.y):
        fruit.refresh_fruit()
        game.score_point()
        #snake.make_snake_bigger()
    game.render_text(screen)
    pygame.display.update()
    clock.tick(6)
