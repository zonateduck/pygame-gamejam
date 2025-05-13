import pygame

class TestScreen2:
    def __init__(self):
        self.areaID = "test02"
        self.objects = []
        self.GREEN = (60, 255, 60)
        self.box_size = 500
        pass


    def run(self, screen):
        #Continously called in the while running-loop.
        pygame.draw.rect(screen, self.GREEN, (200, 100, self.box_size, self.box_size))

    def get_adjacent_area(self, direction):
        match direction:
            case "LEFT": return "test01"
            case "RIGHT": return None
            case "UP" : return None
            case "DOWN" : return None
    
    def get_borders(self):
        return ["RIGHT", "UP", "DOWN"]
    
    def get_objects(self):
        return self.objects
