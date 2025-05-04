import pygame, sys, playerAnimation



class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        #self._layer = PLAYER_LAYER // To make sure the character is drawn above all other layers
        
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x #* TILESIZE (so you can more easily determine spawn position)
        self.y = y #* TILESIZE

        self.width = 'a' #replace with TILESIZE if needed
        self.height = 'a' #replace with TILESIZE if needed

        self.x_change = 0
        self.y_change = 0
        
        #Loads the sprite facing the bottom of the screen
        self.facing = 'down'

        #Starts the sprite in possibly the first animation loop
        #self.animation_loop = 1

        #Cuts out the sprite from the first position of the spritesheet
        self.image = self.game.character_spritesheet.get_sprite(0,0,self.width,self.height)
        
        #Sets hitbox to a rectangle x,y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        Player_animation(self)



    #Movement
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:        #Up
            if not y <= 0:
                self.facing = 'up'
                y -= PLAYER_SPEED #MISSING A VARIABLE PLAYER SPEED 
            else:
                y = 1
        if keys[pygame.K_a]:        #Left
            if not y <= 0:
                self.facing = 'left'
                # x -= PLAYER_SPEED 
            else:
                x = 1
        if keys[pygame.K_s]:        #Down
            if not y >= SCREEN_HEIGHT:
                self.facing = 'down'
                # y += PLAYER_SPEED 
            else:
                y = SCREEN_HEIGHT - 1

        if keys[pygame.K_d]:        #Right
            if not x >= SCREEN_WIDTH:
                self.facing = 'right'
                # x += PLAYER_SPEED 3
            

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    
    def animate(self):
        Player_animation_animate(self)