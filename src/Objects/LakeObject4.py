import pygame

from assets import LAKESPRITE04

SPRITE = LAKESPRITE04
class LakeObject4(pygame.sprite.Sprite):
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID #String, eks. "sol01"
        self.COLOR = (255, 255, 0)
        self.size = 500
        self.x = x
        self.y = y
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size / 2)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        

        self.image = pygame.image.load(SPRITE)
        self.image = pygame.transform.scale(self.image, (self.size * 0.5, self.size))

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

        #if flags["finished_collecting"]:
            #return "play_dialogue", dialogue

        return "go_to_area", "areaID"



        pass

    def update_flags(self):
        pass
