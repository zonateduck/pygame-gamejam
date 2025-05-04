import pygame
from assets import APPLESPRITE

SPRITE = APPLESPRITE
class AppleObject():
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID #String, eks. "sol01"
        self.COLOR = (255, 255, 0)
        self.size = 30
        self.x = x
        self.y = y
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        self.hasBeenCollected = False
        

        self.image = pygame.image.load(SPRITE)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #Suggestions for variables:
        type = "interact eller dialogue"
        dialogue = ["dialogueID"]   #What dialogues are available.
        flags = {}  #Dictionary for various flags
        self.canInteract = True

    def interact(self, world_objects):

        #if flags["finished_collecting"]:
            #return "play_dialogue", dialogue
        world_objects.remove(self)
        print("Removed")
        return world_objects



        pass

    def update_flags(self):
        pass



