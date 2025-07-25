import pygame
from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, RED, WHITE, GREY, BLACK, DARK_GREY

def welcome_screen(win): 
    welcome_font = pygame.font.SysFont('Calibre', 50)  # Larger font for the welcome text      # put fonts
    instruction_font = pygame.font.SysFont('Calibre', 22)  # Smaller font for instructions
    choose_font = pygame.font.SysFont('Calibre', 30)  # Font size for "Choose who starts"

    intro_text1 = welcome_font.render("Welcome to Checkers!", True, WHITE) # Put texts
    intro_text2 = instruction_font.render("The game is played on an 8x8 grid.", True, GREY)
    intro_text3 = instruction_font.render("Red and White take turns to move pieces.", True, GREY)
    intro_text4 = instruction_font.render("You can only move diagonally and capture opponents by jumping.", True, GREY)
    intro_text5 = instruction_font.render("The first player to capture all opponent's pieces wins!", True, GREY)

    intro_rect1 = intro_text1.get_rect(center=(WIDTH // 2, HEIGHT // 4 - 40)) # make texts in center
    intro_rect2 = intro_text2.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 10))
    intro_rect3 = intro_text3.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 40))
    intro_rect4 = intro_text4.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 70))
    intro_rect5 = intro_text5.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 100))

    choose_text = choose_font.render("Choose who starts:", True, WHITE) # put text "Choose who starts"
    choose_rect = choose_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)) # make text in center

    button_width = 180
    button_height = 50
    red_button = Button("Red", WIDTH // 4 - button_width // 2, HEIGHT // 2 + 140, button_width, button_height, RED, BLACK)
    white_button = Button("White", 3 * WIDTH // 4 - button_width // 2, HEIGHT // 2 + 140, button_width, button_height, WHITE, BLACK)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if red_button.is_over(pos):
                    return RED
                elif white_button.is_over(pos):
                    return WHITE

        win.fill(BLACK)  # Fill the window with black
        win.blit(intro_text1, intro_rect1)
        win.blit(intro_text2, intro_rect2)
        win.blit(intro_text3, intro_rect3)
        win.blit(intro_text4, intro_rect4)
        win.blit(intro_text5, intro_rect5)
        win.blit(choose_text, choose_rect)
        red_button.draw(win)
        white_button.draw(win)
        pygame.display.update() # add changes that we made on screen
