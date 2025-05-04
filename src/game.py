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

pygame.display.set_caption("The Colors of Grandma's Forest")

# Clock to control framerate
clock = pygame.time.Clock()
FRAMERATE = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Creates a group for collidable objects    
collidables = pygame.sprite.Group()

# Dialogues variables
FONT = pygame.font.SysFont("lucida console", 24)
TEXT_COLOR = (0, 0, 0)
BOX_COLOR = (180, 180, 200)

# Quest items
#TODO: change the rectangles into objects, and place them around the world
tea = pygame.Rect(200, 400, 30, 30)
apple = pygame.Rect(500, 450, 30, 30)
butterfly = pygame.Rect(300, 300, 30, 30)
tea_visible = apple_visible = butterfly_visible = False

# Game variables
x, y = 100, 100
speed = 8
size = 50

# Dialogue scenes
scenes = [
    (["Iris, my dear... Can you please bring me a cup of tea?", "Of course, Granny!"], ["Granny", "Iris"]),
    (["Iris, honey... I am planning to make apple cake. We will need the reddest of apples!", "I'll get them in the garden!"], ["Granny", "Iris"]),
    (["You know what, child? I always wanted a pet butterfly. Could you find one for me?", "I've seen some in the garden... Maybe I could catch one for you. I'll find the most beautiful one!"], ["Granny", "Iris"]),
    (["You are not my grandma! What did you do to her?!", "Oh, honey, she's just stuck in the painting over the fireplace, don't worry, she's warm and cozy and colorless.",
      "You are the one stealing the colors!", "You catch on quickly... Well, if you want to save dear granny, you will bring me her rainbow scarf.",
      "And if not?", "If not, your dear granny will forever be just a painting...",
      "Why can't you just take it yourself?", "Oh, dearest Iris, I would. You see... Your granny is smart, she protects her belongings. Only you can find the scarf.",
      "She must be vulnerable to color somehow. Let's use the rainbow scarf against her!"],
     ["Iris", "Granny", "Iris", "Granny", "Iris", "Granny", "Iris", "Granny", "Iris"]),
    (["Ahhh... that's just what I needed. Thank you, Iris!"], ["Granny"]),
    (["These apples are perfect! Time to bake some memories!"], ["Granny"]),
    (["What a beautiful butterfly! I shall name her Lacy."], ["Granny"])
]

# Dialogue engine
current_scene = 0
current_line = 0
dialogue_active = False
current_dialogue = ""
current_speaker_side = "right"

def start_dialogue(scene_index):
    global current_scene, current_line, dialogue_active
    current_scene = scene_index
    current_line = 0
    dialogue_active = True
    show_line()

def show_line():
    global current_dialogue, current_speaker_side, dialogue_active
    lines, speakers = scenes[current_scene]
    if current_line < len(lines):
        current_dialogue = lines[current_line]
        current_speaker_side = "left" if speakers[current_line] == "Iris" else "right"
    else:
        dialogue_active = False


# Text display
def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def draw_text_box(text, side):
    box = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)
    pygame.draw.rect(screen, BOX_COLOR, box)
    lines = wrap_text(text, FONT, box.width - 40)
    for i, line in enumerate(lines):
        rendered = FONT.render(line, True, TEXT_COLOR)
        screen.blit(rendered, (box.x + 20, box.y + 20 + i * FONT.get_linesize()))
#    draw_portrait(side)

# TODO: show portraits while talking
#def draw_portrait(side):
#    color = PLAYER_COLOR if side == "left" else NPC_COLOR
#    rect = pygame.Rect(50, 300, 100, 140) if side == "left" else pygame.Rect(WIDTH - 150, 300, 100, 140)
#    pygame.draw.rect(screen, color, rect)

player = Player(screen, x, y, speed)
map = Map(screen)

obj_range = 15   #How big a range the interaction-area has

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
default_area = area_c3 #Should be c3 in the end :)

#This makes sure the game is not in two states at the same time :)
def change_gamestate(new_state):
    global current_state
    global world_borders

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

    tea_visible = quest_stage == 1
    apple_visible = quest_stage == 4
    butterfly_visible = quest_stage == 7

    #TODO: add ITEM pictures!!!!!!!!
    if tea_visible:
        pygame.draw.rect(screen, ITEM_COLOR_1, tea)
        screen.blit(FONT.render("Tea", True, TEXT_COLOR), (tea.x, tea.y - 20))
    if apple_visible:
        pygame.draw.rect(screen, ITEM_COLOR_2, apple)
        screen.blit(FONT.render("Apple", True, TEXT_COLOR), (apple.x, apple.y - 20))
    if butterfly_visible:
        pygame.draw.rect(screen, ITEM_COLOR_3, butterfly)
        screen.blit(FONT.render("Butterfly", True, TEXT_COLOR), (butterfly.x - 10, butterfly.y - 20))


    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if dialogue_active:
                current_line += 1
                show_line()
            else:
                if player.colliderect(npc):
                    if quest_stage == 0:
                        start_dialogue(0)
                        quest_stage = 1
                    elif quest_stage == 2:
                        start_dialogue(4)
                        quest_stage = 3
                    elif quest_stage == 3:
                        start_dialogue(1)
                        quest_stage = 4
                    elif quest_stage == 5:
                        start_dialogue(5)
                        quest_stage = 6
                    elif quest_stage == 6:
                        start_dialogue(2)
                        quest_stage = 7
                    elif quest_stage == 8:
                        start_dialogue(6)
                        quest_stage = 9
                    elif quest_stage == 9:
                        start_dialogue(3)
                        quest_stage = 10

        if player.colliderect(tea) and quest_stage == 1:
            tea_visible = False
            quest_stage = 2

        if player.colliderect(apple) and quest_stage == 4:
            apple_visible = False
            quest_stage = 5

        if player.colliderect(butterfly) and quest_stage == 7:
            butterfly_visible = False
            quest_stage = 8

        if dialogue_active:
            draw_text_box(current_dialogue, current_speaker_side)

        pygame.display.flip()
        clock.tick(60)

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