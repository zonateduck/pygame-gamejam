import pygame
import sys


class Map():
    def __init__(self, screen):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = screen.get_size()
        self.image = pygame.image.load("../assets/map_2.png")
        self.icon = pygame.image.load("../assets/map_icon.png")
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