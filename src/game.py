""" Main game to run """
import pygame
import sys, random, time

from options import *
from assets import *


#Importing levels
from Levels.TestScreen1 import TestScreen1
from Levels.TestScreen2 import TestScreen2
from Levels.StartScreen import StartScreen

from Levels.AreaA1 import AreaA1
from Levels.AreaA6 import AreaA6
from Levels.AreaB1 import AreaB1
from Levels.AreaB2 import AreaB2
from Levels.AreaB3 import AreaB3
from Levels.AreaB5 import AreaB5
from Levels.AreaB6 import AreaB6
from Levels.AreaC2 import AreaC2
from Levels.AreaC3 import AreaC3
from Levels.AreaC4 import AreaC4
from Levels.AreaC5 import AreaC5
from Levels.AreaD3 import AreaD3
from Levels.AreaD4 import AreaD4
from Levels.AreaE4 import AreaE4
from Levels.AreaF4 import AreaF4
from Levels.AreaF5 import AreaF5


#Importing objects
from Objects.TestObject1 import TestObject1
from Objects.TreeObject import TreeObject
from Objects.GrandmaObject import Grandma
from Objects.AppleObject import AppleObject

from colorGrading import *

from player import Player
from map import Map

# Dialogue handles
from interactionsystem import draw_interaction_prompt



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

# Dialogues variables



# Game variables
x, y = 100, 100
speed = 10
size = 50

dialogue_active = False


player = Player(screen, x, y, speed)
map = Map(screen)

obj_range = 15   #How big a range the interaction-area has

grandma = Grandma("GrandmaTest", 900, 700)
objects = {
    # "objectID" : Objekt("mittobjekt1", x, y)
    "testobject01" : TestObject1("testobject01", 200, 300),
    "tree01" : TreeObject("Tree01", 200, 20),
    "apple01" : AppleObject("Apple01", 300, 40),
    "grandma" : grandma
}

#SUGGESTION: Keep a list of objects in the world for the sake of interaction. Update when states change
world_objects = [
    #[object, type, position_x, position_y]
]

world_borders = []  #Updates based on current_state.get_borders()
transition_threshold = 5    #How many pixels off-screen before transition

#GameState manager
#Instantiate EVERYTHING
test_start_screen = StartScreen()
test_screen1 = TestScreen1()
test_screen2 = TestScreen2()

area_a1 = AreaA1()
area_a6 = AreaA6()
area_b1 = AreaB1()
area_b2 = AreaB2()
area_b3 = AreaB3()
area_b5 = AreaB5()
area_b6 = AreaB6()
area_c2 = AreaC2()
area_c3 = AreaC3()
area_c4 = AreaC4()
area_c5 = AreaC5()
area_d3 = AreaD3()
area_d4 = AreaD4()
area_e4 = AreaE4()
area_f4 = AreaF4()
area_f5 = AreaF5()


current_state = test_start_screen


from scene1 import Scene1
test_scene = Scene1(screen)


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
        case "area_a1" : 
            new_state = area_a1
        case "area_a6" : 
            new_state = area_a6
        case "area_b1" : 
            new_state = area_b1
        case "area_b2" : 
            new_state = area_b2
        case "area_b3" : 
            new_state = area_b3
        case "area_b5" : 
            new_state = area_b5
        case "area_b6" : 
            new_state = area_b6
        case "area_c2" : 
            new_state = area_c2
        case "area_c3" : 
            new_state = area_c3
        case "area_c4" : 
            new_state = area_c4
        case "area_c5" : 
            new_state = area_c5
        case "area_d3" : 
            new_state = area_d3
        case "area_d4" : 
            new_state = area_d4
        case "area_e4" : 
            new_state = area_e4
        case "area_f4" : 
            new_state = area_f4
        case "area_f5" : 
            new_state = area_f5
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

    player.update()
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
                    change_gamestate(area_a1)

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
    fake_player_interaction_rect = pygame.Rect(player.x - size/2, player.y - size/2, size + obj_range, size + obj_range)

    screen.blit(player.image, player.rect)
    player.update()
    screen.blit(grandma.image, grandma.rect)

    #   DRAW WORLD OBJECTS 
    #Draw world objects
    for obj in world_objects:
        screen.blit(obj.image, obj.rect)
        #TODO: screen.blit(obj.image, obj.rect) to load the image
    
    for obj in world_objects:
        if fake_player_interaction_rect.colliderect(obj.interaction_rect) and obj.canInteract == True:
            #print("Can interact!")
            #Show text: "Space to talk" (some sort of UI element)
            draw_interaction_prompt(screen)
            # Code to handle interaction 
            if keys[pygame.K_SPACE]:
                # Interaction depending on ID
                if obj.ID == "GrandmaTest":
                    obj.interact()
                    dialogue_active = True
                if obj.ID == "apple01":
                    # pickup
                    pass
                # More interaction with other objects
                
                
            
        #else:
            #print("Cant interact :3")
        
        while dialogue_active == True:
            test_scene.run()
            dialogue_active = not test_scene.is_finished()
    
    
    
    #Draw the UI here
    
    map.run(screen, 600, 200)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
