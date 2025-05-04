""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *


#Importing levels
from Levels.TestScreen1 import TestScreen1
from Levels.TestScreen2 import TestScreen2
from Levels.StartScreen import StartScreen

#Importing objects
from Objects.TestObject1 import TestObject1
from Objects.BlomstObject import BlomstObject
from colorGrading import *

from player import Player
from map import Map


# Initialize pygame
pygame.init()


# Set up the window
WIDTH, HEIGHT = 1280, 720
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

player = Player(screen, x, y, speed)
map = Map(screen)

obj_range = 15   #How big a range the interaction-area has


objects = {
    # "objectID" : Objekt("mittobjekt1", x, y)
    "testobject01" : TestObject1("testobject01", 200, 300),
    "blomst01" : BlomstObject("blomst01", 300, 400),
    "blomst02" : BlomstObject("blomst02", 600, 600),
    "blomst03" : BlomstObject("blomst03", 30, 500),
    "blomst04" : BlomstObject("blomst04", 300, 800),
    "blomst05" : BlomstObject("blomst05", 400, 60)
}

#SUGGESTION: Keep a list of objects in the world for the sake of interaction. Update when states change
world_objects = [
    #[object, type, position_x, position_y]
]

world_borders = []  #Updates based on current_state.get_borders()
transition_threshold = 5    #How many pixels off-screen before transition

#GameState manager
test_start_screen = StartScreen()
test_screen1 = TestScreen1()
test_screen2 = TestScreen2()

current_state = test_start_screen

#This makes sure the game is not in two states at the same time :)
def change_gamestate(new_state):
    global current_state
    global world_borders

    if current_state != new_state:
        world_objects.clear()
        world_borders.clear()
        current_state = new_state
        
        #Update borders and objects:
        world_borders = current_state.get_borders()
        for objectID in current_state.get_objects():
            if objectID in objects.keys():
                world_objects.append(objects[objectID])


def find_area(areaID):
    match areaID:
        case "test01" : 
            new_state = test_screen1
        case "test02" : 
            new_state = test_screen2
        case _: #If areaID did not match
            print("WARNING: Area not found. Create collision in the .get_borders method, or attatch correct area")
            new_state = current_state
    return new_state

#Finds correct area to move to :)
def find_adjacent_area(current_state, direction): 
    areaID = current_state.get_adjacent_area(direction)
    return find_area(areaID)


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                map.toggle_map()
 

    TARGET_COLOR = 		(204,0,0)
    REPLACEMENT_COLOR = (23, 23 ,23)
    # Get key presses

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if not (x < 0 and "LEFT" in world_borders):
            #background = convert_to_black_and_white(background.copy())
            player.x -= speed
            player.facing = "left"
    if keys[pygame.K_d]:
        if not (x > (WIDTH - size) and "RIGHT" in world_borders):
            #background = remove_blue_channel(background.copy())
            player.x += speed
            player.facing = "right"
    if keys[pygame.K_w]:
        if not (y < 0 and "UP" in world_borders):
            #background = remove_red_channel(background.copy())
            player.y -= speed
            player.facing = "up"
    if keys[pygame.K_s]:
        if not (y > (HEIGHT - size) and "DOWN" in world_borders):
            #background = remove_green_channel(background.copy())
            player.y += speed
            player.facing = "down"
    if keys[pygame.K_1]: #DEBUG BUTTON
        background = remove_color(background.copy(), TARGET_COLOR, (160, 160, 160))


    #Draw background
    screen.blit(background, (0, 0))

    #Run the correct gamestate
    #TODO replace test-screens with actual levels / screens
    while current_state == test_start_screen:
        #This doesnt have to be a while loop, but prevents game from moving on :)
        test_start_screen.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("pressed space")
                    change_gamestate(test_screen1)

    if current_state == test_screen1:
        current_state.run(screen) #This makes the current_scene display and do its stuff!
    if current_state == test_screen2:
        current_state.run(screen)

    #Logic for player going to new area :D
    if player.x < 0 - transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "LEFT"))
        player.x = WIDTH
    if player.x > WIDTH + transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "RIGHT"))
        player.x = 0
    if player.y < - transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "UP"))
        player.y = HEIGHT
    if player.y > HEIGHT + transition_threshold:
        change_gamestate(find_adjacent_area(current_state, "DOWN"))
        player.y = 0
        

    # Draw "Player"
    #pygame.draw.rect(screen, BLUE, (x, y, size, size))
    fake_player_interaction_rect = pygame.Rect(x - size/2, y - size/2, size + obj_range, size + obj_range)

    screen.blit(player.image, player.rect)
    player.update()


    #   DRAW WORLD OBJECTS 
    #Draw world objects
    for obj in world_objects:
        pygame.draw.rect(screen, obj.COLOR, (obj.x, obj.y, obj.size, obj.size))
        #TODO: screen.blit(obj.image, obj.rect) to load the image
    
    for obj in world_objects:
        if fake_player_interaction_rect.colliderect(obj.interaction_rect):
            print("Can interact!")
            #TODO: Show text: "Space to talk" (some sort of UI element)
            #TODO: if player presses space:
                # Code to handle interaction
        else:
            print("Cant interact :3")

    #   DRAW DIALOGUE BOXES:
    
    #Draw the UI here
    
    map.run(screen, 600, 200)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
