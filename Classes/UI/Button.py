import pygame


class Btn:
    def __init__(self, x, y, size_x, size_y, color, window):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.window = window
        self.rect = pygame.Rect(x, y, size_x, size_y)

    def check_for_collision(self, mx, my):
        if self.rect.collidepoint((mx, my)):
            return True
        return False

    def draw_button(self):
        pygame.draw.rect(self.window, self.color, self.rect)
