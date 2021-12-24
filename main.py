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
    snake_body = [{
        "x": 200,
        "y": 0,
        "pos": (200, 0)
    }]

    def set_direction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.direction != "down":
                snake.direction = "up"
            if event.key == pygame.K_s and self.direction != "up":
                snake.direction = "down"
            if event.key == pygame.K_a and self.direction != "right":
                snake.direction = "left"
            if event.key == pygame.K_d and self.direction != "left":
                snake.direction = "right"

    def make_snake_bigger(self):
        self.snake_body.append({
            "x": self.snake_body[-1]["pos"][0],
            "y": self.snake_body[-1]["pos"][1],
            "pos": (0, 0)
        })

    def update_snake_body(self, window):
        self.snake_body[0]["x"] = self.x
        self.snake_body[0]["y"] = self.y
        for num in range(1, len(self.snake_body)):
            self.snake_body[num]["x"] = self.snake_body[num - 1]["pos"][0]
            self.snake_body[num]["y"] = self.snake_body[num - 1]["pos"][1]

    def draw_snake(self, window):
        pygame.draw.rect(window, (255, 0, 255), [self.x, self.y, self.snake_width, self.snake_height])
        for num in range(1, len(self.snake_body)):
            pygame.draw.rect(window, (255, 0, 255),
                             [self.snake_body[num]["x"], self.snake_body[num]["y"], self.snake_width,
                              self.snake_height])

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


game = Game()
snake = Snake()
fruit = Fruit()
while True:
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        snake.set_direction(event)

    for node in snake.snake_body:
        node["pos"] = (node["x"], node["y"])

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
    snake.update_snake_body(screen)
    snake.draw_snake(screen)
    if snake.check_fruit_collision(fruit.x, fruit.y):
        fruit.refresh_fruit()
        game.score_point()
        snake.make_snake_bigger()
    game.render_text(screen)
    pygame.display.update()
    clock.tick(30)
