import pygame

from assets import BACKGROUND_B3
BACKGROUND = BACKGROUND_B3

class AreaC3:
    def __init__(self):
        self.areaID = "area_c3"
        self.objects = ["house", "grandma", "tree05"] #Which objects exist in this area?
        
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
            case "LEFT": return "area_c2"
            case "RIGHT": return "area_c4"
            case "UP" : return "area_b3"
            case "DOWN" : return "area_d3"
    
    def get_borders(self):
        return ["UP", "DOWN", "LEFT"]
    
    def get_objects(self):
        return self.objects
    