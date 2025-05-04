import pygame

from assets import BACKGROUND_03
BACKGROUND = BACKGROUND_03

class AreaF5:
    def __init__(self):
        self.areaID = "area_f5"
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
            case "LEFT": return "area_f4"
            case "RIGHT": return None
            case "UP" : return None
            case "DOWN" : return None
    
    def get_borders(self):
        return ["UP", "DOWN", "LEFT"]
    
    def get_objects(self):
        return self.objects
    