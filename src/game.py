""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
