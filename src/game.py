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
from Objects.CatObject import CatObject
from Objects.TreeFruitObject import TreeFruitObject
from Objects.BirdObject import BirdObject
from Objects.Bird2Object import Bird2Object
from Objects.HouseObject import HouseObject
from Objects.LakeObject1 import LakeObject1
from Objects.LakeObject2 import LakeObject2
from Objects.LakeObject3 import LakeObject3
from Objects.LakeObject4 import LakeObject4
from Objects.TutorObject import TutorObject

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

#Creates a group for collidable objects    
collidables = pygame.sprite.Group()

# Dialogues variables



# Game variables
x, y = 100, 100
speed = 8
size = 50

dialogue_active = False


player = Player(screen, x, y, speed)
map = Map(screen)

obj_range = 15   #How big a range the interaction-area has

#grandma = Grandma("GrandmaTest", 900, 700)

objects = {
    # "objectID" : Objekt("mittobjekt1", x, y)
    "apple01" : AppleObject("Apple01", 300, 40),
    "house" : HouseObject("house", 800, 150),
    "grandma" : Grandma("grandma", 810, 330),
    "cat" : CatObject("cat", 1000, 100),
    "treefruit_b6" : TreeFruitObject("treefruit_b6", 600, 20),
    "bird01" : BirdObject("bird01", 300, 100),
    "bird02" : BirdObject("bird01", 20, 400),
    "twobirds01" : Bird2Object("twobirds01", 930, 300),
    "tree01" : TreeObject("tree01", 200, 20),
    "tree02" : TreeObject("tree02", 800, 100),
    "tree03" : TreeObject("tree03", 200, 200),
    "tree04" : TreeObject("tree04", 700, 100),
    "tree05" : TreeObject("tree05", 200, 400),
    "tree06" : TreeObject("tree06", 100, 300),
    "tree07" : TreeObject("tree07", 900, 300),
    "lake01" : LakeObject1("lake01", 630, 290),
    "lake02" : LakeObject2("lake02", 1100, 220),
    "lake03" : LakeObject3("lake03", 0, 370),
    "lake04" : LakeObject4("lake04", 0, 220),
    "tutor" : TutorObject("tutor", 600, 300)
}

#SUGGESTION: Keep a list of objects in the world for the sake of interaction. Update when states change
world_objects = [
    #[object, type, position_x, position_y]
]

world_borders = []  #Updates based on current_state.get_borders()
transition_threshold = 5    #How many pixels off-screen before transition

#GameState manager
#Instantiate EVERYTHING
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


current_progress = "started" #started, searching, collected
talked_to_grandma = False

floors = [area_a1, area_a6, area_b1, area_b2, area_b3, area_b5, area_b6, area_c2, area_c3, area_c5, area_d3, area_d4, area_e4, area_f4, area_f5, area_c4]
objects_to_remove_colors = objects.values()
current_state = test_start_screen
default_area = area_c3 #Should be c3 in the end :)

# DOESNT WORK

from scene1 import Scene1
from scene1a import Scene1a
from scene1b import Scene1b

test_scene = Scene1(screen)
test_scene1a = Scene1a(screen)
test_scene1b = Scene1b(screen)


#This makes sure the game is not in two states at the same time :)
def change_gamestate(new_state):
    global current_state
    global world_borders
    global current_progress

    if current_state != new_state:
        world_objects.clear()
        world_borders.clear()
        collidables.empty()
        current_state = new_state
        
        #Update borders and objects:
        world_borders = current_state.get_borders()
        for objectID in current_state.get_objects():
            if objectID in objects.keys():
                world_objects.append(objects[objectID])
                collidables.add(objects[objectID])
                
        if current_progress == "started" and talked_to_grandma:
            current_progress = "searching"


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
            #print("WARNING: Area not found. Create collision in the .get_borders method, or attatch correct area")
            new_state = default_area
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
#Verdi å gange med for å få diagonal hastighet til å være lik straight:
    v = 0.7071067811865476

    keys = pygame.key.get_pressed()
    dx, dy = 0,0
#Diagonal keybinds

    if keys[pygame.K_a] and keys[pygame.K_w]:
        if not (x < 0 and ("LEFT" in world_borders or "UP" in world_borders)):
            #background = convert_to_black_and_white(background.copy())
            dx = - (speed * v)
            dy = - (speed * v)
            player.facing = "up_left"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
                player.y += dy 
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        if not (x > (WIDTH - size) and ("RIGHT" in world_borders or "UP" in world_borders)):
            #background = remove_blue_channel(background.copy())
            dx += (speed * v)
            dy -= (speed * v)
            player.facing = "up_right"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
                player.y += dy 
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        if not (x < 0 and ("LEFT" in world_borders or "DOWN" in world_borders)):
            #background = convert_to_black_and_white(background.copy())
            dx -= (speed * v)
            dy += (speed * v)
            player.facing = "down_left"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
                player.y += dy 
    elif keys[pygame.K_d] and keys[pygame.K_s]:
        if not (x > (WIDTH - size) and ("RIGHT" in world_borders or "DOWN" in world_borders)):
            #background = remove_blue_channel(background.copy())
            dx += (speed * v)
            dy += (speed * v)
            player.facing = "down_right"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
                player.y += dy 


#Straight keybinds:
    elif keys[pygame.K_a]:
        if not (x < 0 and "LEFT" in world_borders):
            #background = convert_to_black_and_white(background.copy())
            dx -= speed
            player.facing = "left"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
    elif keys[pygame.K_d]:
        if not (x > (WIDTH - size) and "RIGHT" in world_borders):
            #background = remove_blue_channel(background.copy())
            dx += speed
            player.facing = "right"
            if player.can_move_to(dx, dy, collidables):
                player.x += dx
    elif keys[pygame.K_w]:
        if not (y < 0 and "UP" in world_borders):
            #background = remove_red_channel(background.copy())
            dy -= speed
            player.facing = "up"
            if player.can_move_to(dx, dy, collidables):
                player.y += dy 
    elif keys[pygame.K_s]:
        if not (y > (HEIGHT - size) and "DOWN" in world_borders):
            #background = remove_green_channel(background.copy())
            dy += speed
            player.facing = "down"
            if player.can_move_to(dx, dy, collidables):
                player.y += dy 
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
                    change_gamestate(default_area)

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
    #screen.blit(grandma.image, grandma.rect)

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
                if obj.ID == "grandma":
                    obj.interact()
                    dialogue_active = True
                if obj.ID == "apple01":
                    # pickup
                    pass
                # More interaction with other objects
                
                
            
        #else:
            #print("Cant interact :3")

    while dialogue_active == True:
        print("should run")
        if current_progress == "started":
            test_scene.run()
            dialogue_active = not test_scene.is_finished()
            talked_to_grandma = True
        elif current_progress == "searching":
            test_scene1a.run()
            dialogue_active = not test_scene1a.is_finished()
        elif current_progress == "collected":
            test_scene1b.run()
            dialogue_active = not test_scene1b.is_finished()
        
        if dialogue_active == False:
            pygame.time.wait(200)
    
    
    test_scene.dialogue_index = 0
    test_scene1a.dialogue_index = 0
    test_scene1b.dialogue_index = 0
    #Draw the UI here
    
    map.run(screen, 600, 200)

    # Update display
    pygame.display.flip()


# Clean up
pygame.quit()
sys.exit()