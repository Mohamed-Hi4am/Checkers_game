import pygame
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8 
SQUARE_SIZE = WIDTH//COLS #10

RED = (255, 0, 0 )
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BINK = (255, 153, 204 )
DARK_GREY =  (170,170,170)
FPS = 60
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (33, 20))