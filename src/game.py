""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *

from TestScreen1 import TestScreen1
from TestScreen2 import TestScreen2
from TestStartScreen import TestStartScreen

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


#GameState manager
test_start_screen = TestStartScreen()
test_screen1 = TestScreen1()
test_screen2 = TestScreen2()

current_state = test_start_screen

def change_gamestate(new_state):
    #This makes sure the game is not in two states at the same time :)
    global current_state
    if current_state != new_state:
        if current_state != None:
            current_state.exit()    #UNUSED: We might not want exit/enter methods, depends where we want to keep important gamedata.
        current_state = new_state
        current_state.enter()       #Also unused

    #SUGGESTION: current_state.get_borders() updates some variables for borders here in the main :)

#Finds correct area to move to :)
def find_adjacent_area(current_state, direction): 
    areaID = current_state.get_adjacent_area(direction)

    match areaID:
        case "test01" : 
            new_state = test_screen1
        case "test02" : 
            new_state = test_screen2
        case _: #If areaID did not match
            print("Warning: Area not found. Create collision?")
            new_state = current_state
    return new_state


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

    #Draw background
    screen.fill(WHITE)

    #Run the correct gamestate
    #TODO replace test-screens with actual levels / screens
    while current_state == test_start_screen:
        #This doesnt have to be a while loop, but prevents game from moving on :)
        test_start_screen.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("pressed space")
                    change_gamestate(test_screen1)
        pygame.display.flip()

    if current_state == test_screen1:
        current_state.run(screen) #This makes the current_scene display and do its stuff!
    if current_state == test_screen2:
        current_state.run(screen)

    #Logic for player going to new area :D
    if x < 0:
        current_state = find_adjacent_area(current_state, "LEFT")
        x = WIDTH
    if x > WIDTH:
        current_state = find_adjacent_area(current_state, "RIGHT")
        x = 0
    if y < 0:
        current_state = find_adjacent_area(current_state, "UP")
        y = HEIGHT
    if y > HEIGHT:
        find_adjacent_area(current_state, "DOWN")
        y = 0
        

    # Draw "Player"
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
