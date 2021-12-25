import pygame
import random


class Fruit:
    WIDTH = 1000
    HEIGHT = 1000
    FRUIT_WIDTH = 50
    FRUIT_HEIGHT = 50
    FRUIT_COLOR = (255, 255, 255)
    x = random.randrange(0, WIDTH - FRUIT_WIDTH, 50)
    y = random.randrange(0, HEIGHT - FRUIT_HEIGHT, 50)

    def refresh_fruit(self):
        self.x = random.randrange(0, self.WIDTH - self.FRUIT_WIDTH, 50)
        self.y = random.randrange(0, self.HEIGHT - self.FRUIT_HEIGHT, 50)

    def draw_fruit(self, window):
        pygame.draw.rect(window, self.FRUIT_COLOR, [self.x, self.y, self.FRUIT_WIDTH, self.FRUIT_HEIGHT])
