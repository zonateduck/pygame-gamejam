

import math, pygame #, sprites


def Player_animation(self):

    self.up_animation = [
    #Gets the sprite from the sheet at this    x  y  and character size
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
    ]

    self.left_animation = [
    #Gets the sprite from the sheet at this    x  y  and character size
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
    ]

    self.down_animation = [
    #Gets the sprite from the sheet at this    x  y  and character size
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
    ]

    self.right_animation = [
    #Gets the sprite from the sheet at this    x  y  and character size
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
    ]

def Player_animation_animate(self):

    if self.facing == 'up':
        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)


        else:
            #Sets the image as self.down sprite according to the rounded down of the animation loop
            self.image = self.up_animation[math.floor(self.animation_loop)]

            #The animation loop:
            self.animation_loop += 0.1
            if self.animation_loop >= 3:    # 3 is a placeholder for the amount of sprites we want to use in each animation
                self.animation_loop = 1     # Resets spriteanimation to the start of it

    if self.facing == 'left':
        if self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        else:
            self.image = self.left_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:   
                self.animation_loop = 1    

    
    if self.facing == 'down':
        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        else:
            self.image = self.down_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:    
                self.animation_loop = 1     

    
    if self.facing == 'right':
        if self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        else:
            self.image = self.right_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:    
                self.animation_loop = 1     

    
    

