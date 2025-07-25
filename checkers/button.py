import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, text_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.SysFont('Calibre', 35)

    def draw(self, win): # draw button                     # draw background of button
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, 100) # 0 -> full button # 100 -> radius
        text_surface = self.font.render(self.text, True, self.text_color) # put text
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2)) # make text in center
        win.blit(text_surface, text_rect)  # draw text on button

    def is_over(self, pos):
        x, y = pos
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height
