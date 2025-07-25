import pygame
from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, RED, WHITE, BLACK, DARK_GREY, GREEN

def display_winner(winner_color, win):
    font = pygame.font.SysFont('Calibre', 50)
    if winner_color == WHITE:
        color = "White"
    else:
        color = "Red"
    winner_text = font.render(f"{color} Wins!", True, WHITE) # text
    winner_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 4)) #pos of text

    button_width = 180
    button_height = 50

    restart_button = Button("Restart", WIDTH // 2 - button_width // 2, HEIGHT // 2 - 60, button_width, button_height, GREEN, BLACK)
    exit_button = Button("Exit", WIDTH // 2 - button_width // 2, HEIGHT // 2 + 10, button_width, button_height, DARK_GREY, BLACK)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.is_over(pos):
                    return True  # Restart the game
                elif exit_button.is_over(pos):
                    pygame.quit()
                    return False

        win.fill((0, 0, 0)) # Fill the window with black
        win.blit(winner_text, winner_rect) # DRAW TEXT POSITION
        restart_button.draw(win)
        exit_button.draw(win)
        pygame.display.update() # add changes that we made on screen
