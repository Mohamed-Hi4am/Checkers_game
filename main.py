import pygame
from checkers.constants import RED, WHITE, WIDTH, HEIGHT, FPS, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game
from checkers.welcome_screen import welcome_screen
from checkers.display_winner import display_winner
from checkers.button import Button

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Set window size
pygame.display.set_caption('Checkers')

# Initialize pygame and font module
pygame.init()
pygame.font.init()  # Make sure to initialize the font module

# Get row and column from mouse position
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock() # for fixed speed not quickly

    # Start the game by showing the welcome screen and choosing who goes first
    first_turn = welcome_screen(WIN) #red white # Show the welcome screen and get the starting color

    while run:
        game = Game(WIN, first_turn)  # Create a new game with the selected starting color

        while True:  # This inner loop will continue until the game is over
            clock.tick(FPS)

            # Handle events during the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # catch the window close event (the "X" button)
                    run = False  # to break out of the game loop and quit
                    pygame.quit()  # Ensure pygame is quit
                    # break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    if not game.select(row, col): # True False
                        game.clear_valid_moves()  # Clear valid moves if selection is invalid

            if game.winner() is not None:  # none red white
                winner = game.winner() # RED WHITE
                # print(f'{winner} wins!')
                if not display_winner(winner, WIN):  # Display winner screen and ask if the user wants to restart
                    run = False  # Exit the game if the user chooses exit
                    pygame.quit()  # Ensure pygame is quit
                    #break
                else:
                    first_turn = welcome_screen(WIN)  # Show the welcome screen again to choose who starts
                    break  # Break out of the game loop to reset the game

            game.update()  # Update the game state

        if not run:
            break  # Exit the outer loop after quitting

    pygame.quit()

if __name__ == "__main__":
    main()
