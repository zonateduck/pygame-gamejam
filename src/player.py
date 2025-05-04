import pygame, sys, playerAnimation

from assets import PLAYERSPRITE_UP
from assets import PLAYERSPRITE_LEFT
from assets import PLAYERSPRITE_RIGHT
from assets import PLAYERSPRITE_DOWN



#TODO: remove


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        screen_height, screen_width = screen.get_size()
        self.SCREEN_HEIGHT = screen_height
        self.SCREEN_WIDTH = screen_width
        self.PLAYER_SPEED = speed
        self.size = (150, 150)
        #self.game = game
        
        self.playersprite = PLAYERSPRITE_DOWN

        #self.groups = self.game.all_sprites
        #pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x #* TILESIZE (so you can more easily determine spawn position)
        self.y = y #* TILESIZE

        self.width = 100 #replace with TILESIZE if needed
        self.height = 100  #replace with TILESIZE if needed

        self.x_change = 0
        self.y_change = 0
        
        #Loads the sprite facing the bottom of the screen
        self.facing = 'down'

        #Starts the sprite in possibly the first animation loop
        #self.animation_loop = 1

        #Cuts out the sprite from the first position of the spritesheet
        #self.image = self.game.player_sprite.get_sprite(0,0, self.width, self.height)
        #Placeholder garfield:
        self.image = pygame.image.load(self.playersprite)
        self.image = pygame.transform.scale(self.image, self.size)


        #Sets hitbox to a rectangle x,y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #Player_animation(self)



    #Movement
    """
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:        #Up
            if not self.y <= 0:
                self.facing = 'up'
                self.y -= self.PLAYER_SPEED #MISSING A VARIABLE PLAYER SPEED 
            else:
                self.y = 1
        if keys[pygame.K_a]:        #Left
            if not self.y <= 0:
                self.facing = 'left'
                self.x -= self.PLAYER_SPEED 
            else:
                self.x = 1
        if keys[pygame.K_s]:        #Down
            if not self.y >= self.SCREEN_HEIGHT:
                self.facing = 'down'
                self.y += self.PLAYER_SPEED 
            else:
                self.y = self.SCREEN_HEIGHT - 1

        if keys[pygame.K_d]:        #Right
            if not self.x >= self.SCREEN_WIDTH:
                self.facing = 'right'
                self.x += self.PLAYER_SPEED
        print(str(self.x) + ", " + str(self.y))

        """

    def update(self):
        #self.move()
        #self.animate()

        if self.facing == "right":
            print("moving right")
            self.playersprite = PLAYERSPRITE_RIGHT
        if self.facing == "left":
            self.playersprite = PLAYERSPRITE_LEFT
        if self.facing == "down":
            self.playersprite = PLAYERSPRITE_DOWN
        if self.facing == "up":
            self.playersprite = PLAYERSPRITE_UP  
            
        self.rect.x = self.x
        self.rect.y = self.y

        #self.x_change = 0
        #self.y_change = 0
        self.image = pygame.image.load(self.playersprite)
        self.image = pygame.transform.scale(self.image, self.size)
