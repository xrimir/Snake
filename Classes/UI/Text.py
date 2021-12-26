import pygame


class Text:
    font_arial = pygame.font.SysFont("Arial", 25)

    def __init__(self, text, x, y, window, align_center=False):
        self.text = text
        self.x = x
        self.y = y
        self.window = window
        self.align_center = align_center

    def draw_text(self):
        text_render = self.font_arial.render(self.text, True, (255, 255, 255))
        if self.align_center:
            self.window.blit(text_render,
                             (self.x - text_render.get_size()[0] // 2, self.y - text_render.get_size()[1] // 2))
        else:
            self.window.blit(text_render, (self.x, self.y))