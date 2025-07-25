import pygame
from .constants import RED, WHITE, GREEN, SQUARE_SIZE, GREY, ROWS, COLS
from checkers.board import Board

class Game:
    def __init__(self, win, first_turn ):
        self._init(first_turn)
        self.win = win
    
    def update(self):
        self.board.draw(self.win, selected_piece=self.selected)
        self.draw_valid_moves(self.valid_moves) # Green -> moves={}
        pygame.display.update()

    def _init(self,first_turn ):
        self.selected = None
        self.board = Board()
        self.turn = first_turn 
        self.valid_moves = {}
        
    def winner(self):
        # Check if current player has no valid moves
        if self.has_no_valid_moves(self.turn):
            winner_color = WHITE if self.turn == RED else RED
            return winner_color
        return None

    def reset(self, first_turn):
        self._init(first_turn)

    def select(self, row, col): # if select any piece or square
        if self.selected: # none RED WHITE -> green
            result = self._move(row, col) # if exist valid moves (green)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col) # first 0 RED WHITE
        if piece != 0 and piece.color == self.turn: # turn = first_turn
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece) # moves={}
            return True
            
        return False

    def _move(self, row, col): # MOVE TO
        piece = self.board.get_piece(row, col) # 0 RED WHITE
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves): # Green -> moves={}
        for move in moves:
            row, col = move # key is tuple (row , col)   =
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 17)

    def change_turn(self):
        self.valid_moves = {} # CLEAR For move={}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def clear_valid_moves(self):
        self.valid_moves = {}

    def has_no_valid_moves(self, color):
            # Check if the player has no valid moves
            for row in range(ROWS):
                for col in range(COLS):
                    piece = self.board.get_piece(row, col) #0 RED WHITE
                    if piece != 0 and piece.color == color:
                        if self.board.get_valid_moves(piece):  # If any piece has valid moves, return False
                            return False
            return True  # If no piece has valid moves

    # def is_selected(self, piece): # return true false
    #     return piece == self.selected # 0 red white
    