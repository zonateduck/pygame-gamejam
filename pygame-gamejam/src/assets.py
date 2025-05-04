import os
import pygame

script_dir = os.path.dirname(__file__)  # the folder this script is in
asset_path = os.path.join(script_dir, "..", "assets", "colorgradingtest.png")

BACKGROUND = asset_path

# Objects

path = ".."

BLOMSTSPRITE = path + "/assets/flower.jpeg"
GRANDMASPRITE = path  + "/assets/grandma little slouch.png"

PLAYERSPRITE_UP = path  + "/assets/iris up.png"
PLAYERSPRITE_LEFT = path  + "/assets/iris straight left.png"
PLAYERSPRITE_RIGHT = path  + "/assets/iris straight right.png"
PLAYERSPRITE_DOWN = path  + "/assets/iris down.png"
PLAYERSPRITE_DOWNRIGHT = path  + "/assets/iris down right.png"
PLAYERSPRITE_DOWNLEFT = path  + "/assets/iris down left.png"


TREESPRITE = path + "/assets/tree.png"
APPLESPRITE = path + "/assets/apple.jpg"