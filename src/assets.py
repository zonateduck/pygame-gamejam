import os
import pygame

script_dir = os.path.dirname(__file__)  # the folder this script is in
asset_path = os.path.join(script_dir, "..", "assets", "colorgradingtest.png")

BACKGROUND = asset_path

# Objects

path = ".."

BLOMSTSPRITE = path + "/assets/flower.jpeg"
GRANDMASPRITE = path  + "/assets/grandma little slouch.png"

PLAYERSPRITE_UP = path  + "/assets/iris right.png"
PLAYERSPRITE_LEFT = path  + "/assets/iris back.png"
PLAYERSPRITE_RIGHT = path  + "/assets/iris forward right.png"
PLAYERSPRITE_DOWN = path  + "/assets/iris left.png"


TREESPRITE = path + "/assets/tree.png"
FRUITTREESPRITE = path + "/assets/tree with fruit.png"
APPLESPRITE = path + "/assets/apple.jpg"
GARFIELDSPRITE = path + "/assets/garfield.png"
BIRDSPRITE = path + "/assets/bird.png"
TWOBIRDSPRITE = path + "/assets/two birds.png"


BACKGROUND_02 = path + "/assets/background2.png"
BACKGROUND_03 = path + "/assets/background3.png"
BACKGROUND_04 = path + "/assets/background4.png"
BACKGROUND_05 = path + "/assets/background5.png"
BACKGROUND_L1 = path + "/assets/background_lake1.png"
BACKGROUND_L2 = path + "/assets/background_lake2.png"
BACKGROUND_B1 = path + "/assets/background_basic1.png"
BACKGROUND_B2 = path + "/assets/background_basic2.png"
BACKGROUND_B3 = path + "/assets/background_basic3.png"