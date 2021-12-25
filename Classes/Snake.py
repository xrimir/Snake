import pygame


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
                self.direction = "up"
            if ev.key == pygame.K_s and self.direction != "up":
                self.direction = "down"
            if ev.key == pygame.K_a and self.direction != "right":
                self.direction = "left"
            if ev.key == pygame.K_d and self.direction != "left":
                self.direction = "right"

    def move_snake(self):
        if self.direction == "up":
            self.y -= self.VELOCITY
        elif self.direction == "down":
            self.y += self.VELOCITY
        elif self.direction == "left":
            self.x -= self.VELOCITY
        elif self.direction == "right":
            self.x += self.VELOCITY

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
