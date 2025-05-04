import pygame

from assets import BACKGROUND_04
BACKGROUND = BACKGROUND_04

class AreaB5:
    def __init__(self):
        self.areaID = "area_b5"
        self.objects = [] #Which objects exist in this area?
        
        self.background = pygame.image.load(BACKGROUND)
        
        self.font = pygame.font.SysFont(None, 25)
        self.text_debug = self.font.render(self.areaID, True, (0, 0, 0))


    def run(self, screen):
        #Continously called in the while running-loop.
        screen.blit(self.background, (0, 0))
        screen.blit(self.text_debug, (0, 0))
        #Draw the background here


    def get_adjacent_area(self, direction):
        match direction:
            case "LEFT": return None
            case "RIGHT": return "area_b6"
            case "UP" : return None
            case "DOWN" : return "area_c5"
    
    def get_borders(self):
        return ["UP", "DOWN", "LEFT"]
    
    def get_objects(self):
        return self.objects
    