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
APPLESPRITE = path + "/assets/apple.jpg"