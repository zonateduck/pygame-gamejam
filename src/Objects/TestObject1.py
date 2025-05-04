import pygame


SPRITE = "../assets/houseplaceholder.png"

class TestObject1():
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID #string
        self.COLOR = (255, 255, 0)
        self.size = 5
        self.x = x
        self.y = y
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        self.size = ()
        

        self.image = pygame.image.load(SPRITE)
        # Controls scale
        # self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #Suggestions for variables:
        type = "interact eller dialogue"
        dialogue = ["dialogueID"]   #What dialogues are available.
        flags = {}  #Dictionary for various flags
    
        # Handles interaction
        self.canInteract = False

    def canInteract(self):
        return self.canInteract

    def interact(self):
        pass

    def update_flags(self):
        pass



