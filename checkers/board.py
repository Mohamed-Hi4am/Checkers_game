import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, DARK_GREY
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12  # num of remaining_pieces
        self.red_kings = self.white_kings = 0  # num of kings
        self.create_board()
    
    def draw_squares(self, win): # draw squares on window
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, DARK_GREY, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #

    def move(self, piece, row, col): # move piece from current pos to new pos 
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0: # make king is true and k++
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col] # 0 RED WHITE

    def create_board(self): # put pieces in a 2 dimensional board else put 0
        for row in range(ROWS):
            self.board.append([]) #
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, win, selected_piece=None): #draw board and all pieces
        self.draw_squares(win) #draw board
        for row in range(ROWS): #draw all pieces
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    is_selected = (piece == selected_piece) # if selected = 1 add double outlier
                    piece.draw(win, selected=is_selected)


    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    # def winner(self):
    #     if self.red_left <= 0:
    #         return WHITE
    #     elif self.white_left <= 0:
    #         return RED
    #
    #     return None
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]

            # If the square is empty, check if it's a valid jump or regular move
            if current == 0:
                if skipped and not last: # skipped contains a piece
                    break                # last is empty
                elif skipped:
                    moves[(r, left)] = last + skipped # If we have skipped an opponent's piece
                else:
                    moves[(r, left)] = last  #Just move without skipping anything

                # If we have skipped a piece, continue traversing to check for further jumps
                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            # If we encounter a piece of the same color, we can't jump over it
            elif current.color == color:
                break
            else:
                last = [current] # Opponent's piece is encountered, so store it in last

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
    