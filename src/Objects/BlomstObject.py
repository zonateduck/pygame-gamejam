import pygame

GRANDMA_SPRITE = "pygame-gamejam/assets/grandma.png"
class BlomstObject():
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID #String
        self.COLOR = (0, 255, 0)
        self.size = 50
        self.x = x
        self.y = y
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        
        #Suggestions for variables:
        type = "interact eller dialogue"
        dialogue = ["dialogueID"]   #What dialogues are available.
        flags = {}  #Dictionary for various flags
    
        self.image = pygame.image.load(GRANDMA_SPRITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def interact(self):
        pass


    def update_flags(self):
        pass



