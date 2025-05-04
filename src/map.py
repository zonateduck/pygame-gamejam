import pygame
import sys

from assets import MAP
from assets import MAP_ICON

MAPSPRITE = MAP
MAPICON = MAP_ICON

class Map():
    def __init__(self, screen):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = screen.get_size()
        self.image = pygame.image.load(MAPSPRITE)
        self.icon = pygame.image.load(MAPICON)
        self.visible = False
        
    def run(self, screen, x, y):
        if self.visible:
            screen.blit(self.image, (x, y))
        screen.blit(self.icon, (self.SCREEN_WIDTH - 200, 10))
    
    def toggle_map(self):
        if self.visible:
            self.visible = False
        else:
            self.visible = True