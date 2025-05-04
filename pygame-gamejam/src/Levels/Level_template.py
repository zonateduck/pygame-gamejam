import pygame

class TestScreen1:
    def __init__(self):
        self.areaID = "template01"
        self.objects = ["testobject01"] #Which objects exist in this area?
        self.RED = (255, 60, 60)
        self.box_size = 500
        pass

    def enter(self):
        #Called when state is entered.
        pass

    def run(self, screen):
        #Continously called in the while running-loop.
        pygame.draw.rect(screen, self.RED, (100, 200, self.box_size, self.box_size))

    def get_adjacent_area(self, direction):
        match direction:
            case "LEFT": return None
            case "RIGHT": return "test02"
            case "UP" : return None
            case "DOWN" : return None
    
    def get_borders(self):
        return ["UP", "DOWN", "LEFT"]
    
    def get_objects(self):
        return self.objects
    
    def exit(self):
        #Called when state is exited.
        pass