""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *

#Importing levels
from TestScreen1 import TestScreen1
from TestScreen2 import TestScreen2
from TestStartScreen import TestStartScreen

#Importing objects
from TestObject1 import TestObject1

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

objects = {
    "testobject01" : TestObject1()
}

#SUGGESTION: Keep a list of objects in the world for the sake of interaction. Update when states change
world_objects = [
    #[object, type, position_x, position_y]
]

world_borders = []  #Updates based on current_state.get_borders()
transition_threshold = 5    #How many pixels off-screen before transition

#GameState manager
test_start_screen = TestStartScreen()
test_screen1 = TestScreen1()
test_screen2 = TestScreen2()

current_state = test_start_screen

def change_gamestate(new_state):
    #This makes sure the game is not in two states at the same time :)
    global current_state
    global world_borders

    if current_state != new_state:
        if current_state != None:
            current_state.exit()    #UNUSED: We might not want exit/enter methods, depends where we want to keep important gamedata.
        current_state = new_state
        current_state.enter()       #Also unused

        #SUGGESTION: update a list of borders here in the main :)
        world_borders = current_state.get_borders()

        world_objects.clear()
        for objectID in current_state.get_objects():
            if objectID in objects.keys():
                world_objects.append(objects[objectID])

#Finds correct area to move to :)
def find_adjacent_area(current_state, direction): 
    areaID = current_state.get_adjacent_area(direction)

    match areaID:
        case "test01" : 
            new_state = test_screen1
        case "test02" : 
            new_state = test_screen2
        case _: #If areaID did not match
            print("WARNING: Area not found. Create collision in the .get_borders method, or attatch correct area")
            new_state = current_state
    return new_state

def draw_world_objects():
    pass

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
        if not (x < 0 and "LEFT" in world_borders):
            x -= speed
    if keys[pygame.K_RIGHT]:
        if not (x > (WIDTH - size) and "RIGHT" in world_borders):
            x += speed
    if keys[pygame.K_UP]:
        if not (y < 0 and "UP" in world_borders):
            y -= speed
    if keys[pygame.K_DOWN]:
        if not (y > (HEIGHT - size) and "DOWN" in world_borders):
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
    if x < 0 - transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "LEFT"))
        x = WIDTH
    if x > WIDTH + transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "RIGHT"))
        x = 0
    if y < - transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "UP"))
        y = HEIGHT
    if y > HEIGHT + transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "DOWN"))
        y = 0
        

    # Draw "Player"
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    for obj in world_objects:
        pygame.draw.rect(screen, obj.COLOR, (obj.pos_x, obj.pos_y, obj.size, obj.size))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
