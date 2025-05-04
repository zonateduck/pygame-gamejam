import pygame

#Important to create the objects in the levels as such:

#        wall = TestObject1(300, 300)
#        world_objects.append(wall)
#        collidables.add(wall)  # Ïmportant!! Add it do the collidables group!


class TestObject1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ID = "testobject01"
        self.COLOR = (255, 255, 0)
        self.size = 120
        self.x = 50
        self.y = 50
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        
        #self.collison_enabled = True/False (det vi vil objektet skal være)

        #Suggestions for variables:
        type = "interact eller dialogue"
        dialogue = ["dialogueID"]   #What dialogues are available.
        flags = {}  #Dictionary for various flags
    

    def interact(self):
        pass

    def update_flags(self):
        pass



