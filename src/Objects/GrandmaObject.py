import pygame
import os


script_dir = os.path.dirname(__file__)  # the folder this script is in
asset_path = os.path.join(script_dir, "..", "assets", "grandma.png")
GRANDMA_SPRITE = "pygame-gamejam/assets/grandma.png"

class Grandma():
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID #String, eks. "sol01"
        self.COLOR = (255, 255, 0)
        self.size = 120
        self.x = x
        self.y = y
        self.collision_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.interaction_rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size * 1.5, self.size * 1.5)
        self.dialoguesToPlay = 0
        self.grandmasprite = GRANDMA_SPRITE

        self.image = pygame.image.load(GRANDMA_SPRITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #Suggestions for variables:
        type = "interact eller dialogue"
        dialogue = ["dialogueID"]   #What dialogues are available.
        flags = {}  #Dictionary for various flags
    

    def interact(self):

        #if flags["finished_collecting"]:
            #return "play_dialogue", dialogue

        return "go_to_area", "areaID"



        pass

    def update_flags(self):
        pass



