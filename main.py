import sys
import random
import pygame
import time

pygame.init()
pygame.font.init()
SIZE = WIDTH, HEIGHT = 1000, 1000
game_status = True
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")


class Game:
    score = 0

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


class Snake:
    x = 200
    y = 0

    SNAKE_WIDTH = 50
    SNAKE_HEIGHT = 50
    SNAKE_HEAD_COLOR = (255, 255, 0)
    SNAKE_TAIL_COLOR = (255, 0, 255)
    VELOCITY = 50
    direction = ""
    snake_body = [{
        "x": 200,
        "y": 0,
        "pos": (200, 0)
    }]

    def set_direction(self, ev):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w and self.direction != "down":
                snake.direction = "up"
            if ev.key == pygame.K_s and self.direction != "up":
                snake.direction = "down"
            if ev.key == pygame.K_a and self.direction != "right":
                snake.direction = "left"
            if ev.key == pygame.K_d and self.direction != "left":
                snake.direction = "right"

    def snake_grow(self):
        self.snake_body.append({
            "x": self.snake_body[-1]["pos"][0],
            "y": self.snake_body[-1]["pos"][1],
            "pos": (0, 0)
        })

    def move_tail(self, window):
        self.snake_body[0]["x"] = self.x
        self.snake_body[0]["y"] = self.y
        for num in range(1, len(self.snake_body)):
            self.snake_body[num]["x"] = self.snake_body[num - 1]["pos"][0]
            self.snake_body[num]["y"] = self.snake_body[num - 1]["pos"][1]

    def draw_snake(self, window):
        pygame.draw.rect(window, self.SNAKE_HEAD_COLOR, [self.x, self.y, self.SNAKE_WIDTH, self.SNAKE_HEIGHT])
        for num in range(1, len(self.snake_body)):
            pygame.draw.rect(window, self.SNAKE_TAIL_COLOR,
                             [self.snake_body[num]["x"], self.snake_body[num]["y"], self.SNAKE_WIDTH,
                              self.SNAKE_HEIGHT])

    def check_fruit_collision(self, fruit_x, fruit_y):
        if self.x == fruit_x and self.y == fruit_y:
            return True
        else:
            return False


class Fruit:
    FRUIT_WIDTH = 50
    FRUIT_HEIGHT = 50
    FRUIT_COLOR = (255, 255, 255)
    x = random.randrange(0, WIDTH - FRUIT_WIDTH, 50)
    y = random.randrange(0, HEIGHT - FRUIT_HEIGHT, 50)

    def refresh_fruit(self):
        self.x = random.randrange(0, WIDTH - self.FRUIT_WIDTH, 50)
        self.y = random.randrange(0, HEIGHT - self.FRUIT_HEIGHT, 50)

    def draw_fruit(self, window):
        pygame.draw.rect(window, self.FRUIT_COLOR, [self.x, self.y, self.FRUIT_WIDTH, self.FRUIT_HEIGHT])


game = Game()
snake = Snake()
fruit = Fruit()
while game_status:
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        snake.set_direction(event)

    for node in snake.snake_body:
        node["pos"] = (node["x"], node["y"])

    if snake.direction == "up":
        snake.y -= snake.VELOCITY
    elif snake.direction == "down":
        snake.y += snake.VELOCITY
    elif snake.direction == "left":
        snake.x -= snake.VELOCITY
    elif snake.direction == "right":
        snake.x += snake.VELOCITY
    if snake.y < 0:
        game_status = False
    elif snake.x < 0:
        game_status = False
    elif (snake.y + snake.VELOCITY) + snake.SNAKE_HEIGHT // 2 > HEIGHT:
        game_status = False
    elif (snake.x + snake.VELOCITY) + snake.SNAKE_WIDTH // 2 > WIDTH:
        game_status = False
    for num in range(1, len(snake.snake_body)):
        if snake.x == snake.snake_body[num]["x"] and snake.y == snake.snake_body[num]["y"]:
            game_status = False
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