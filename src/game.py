""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *
from colorGrading import *

# Initialize pygame
pygame.init()


# Set up the window
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
GAME_BACKGROUND = BACKGROUND
background = pygame.transform.scale(pygame.image.load(GAME_BACKGROUND).convert(), (WIDTH, HEIGHT))


# TODO: make up a name for our game
pygame.display.set_caption("Our game name")

# Clock to control framerate
clock = pygame.time.Clock()
FRAMERATE = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

    



# Game variables
x, y = 100, 100
speed = 5
size = 50

# Game loop
running = True
while running:
    clock.tick(FRAMERATE)  # Limit frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    TARGET_COLOR = 		(204,0,0)
    REPLACEMENT_COLOR = (23, 23 ,23)
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background = convert_to_black_and_white(background.copy())
    if keys[pygame.K_RIGHT]:
        background = remove_blue_channel(background.copy())
    if keys[pygame.K_UP]:
        background = remove_red_channel(background.copy())
    if keys[pygame.K_DOWN]:
        background = remove_green_channel(background.copy())
    if keys[pygame.K_s]:
        background = remove_color(background.copy(), TARGET_COLOR, (160, 160, 160))

    # Draw
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
