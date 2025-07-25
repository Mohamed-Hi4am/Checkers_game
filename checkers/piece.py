from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    # This would typically calculate the position on the screen based on row and col
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win, selected=False):
        radius = SQUARE_SIZE // 2 - self.PADDING
        outline = self.OUTLINE * 2 if selected else self.OUTLINE  # Double outline for selected pieces
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + outline)  # Outer border
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # Inner circle
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))


    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self): # represent piece with color
        return str(self.color)
    