import pygame
import sys

from sound import *
from assets import GRANDMA
from assets import IRIS
from assets import BACKGROUND

# Image paths (replace with actual file paths)
GRANDMAPORTRAIT = GRANDMA  # Replace with the actual path
IRISPORTRAIT = IRIS  # Replace with the actual path
BACKGROUND1 = BACKGROUND

noise = Sound()

# Screen settings
class Scene1:
    def __init__(self, screen):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = screen.get_size()
        self.FONT = pygame.font.SysFont("lucida console", 24)
        self.TEXT_COLOR = (255, 255, 255)
        self.BOX_COLOR = (0, 0, 0)
        self.BOX_PADDING = 20
        self.finished = True

        # Dialogue content
        self.dialogue = [
            "Iris, my dear... Can you please bring me a cup of tea?",
            "Of course, Granny!"
        ]

        self.speakers = [
    "Granny",
    "Iris"
]

        self.dialogue_index = 0
        self.screen = screen  # Keep track of the screen passed from main

        # Portrait size and position logic
        self.PORTRAIT_WIDTH = 120
        self.PORTRAIT_HEIGHT = 160

        # Load portraits
        self.granny_portrait = pygame.image.load(GRANDMAPORTRAIT)
        self.iris_portrait = pygame.image.load(IRISPORTRAIT)
        
        # Scale portraits if necessary
        self.granny_portrait = pygame.transform.scale(self.granny_portrait, (self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT))
        self.iris_portrait = pygame.transform.scale(self.iris_portrait, (self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT))


        # Test
        self.background = pygame.image.load(BACKGROUND1).convert()
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

       
    def clear_portrait_area(self):
        self.portrait_y = self.SCREEN_HEIGHT - 170 - self.PORTRAIT_HEIGHT

        # Clear left portrait area by redrawing the background portion
        if hasattr(self, 'background'):
            iris_rect = pygame.Rect(50, self.portrait_y, self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT)
            self.screen.blit(self.background, iris_rect.topleft, iris_rect)
            
            granny_rect = pygame.Rect(self.SCREEN_WIDTH - 50 - self.PORTRAIT_WIDTH, self.portrait_y, self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT)
            self.screen.blit(self.background, granny_rect.topleft, granny_rect)
        else:
            # If no background image, use background color
            bg_color = (100, 100, 255)  # Or whatever your default background color is
            iris_rect = pygame.Rect(50, self.portrait_y, self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT)
            pygame.draw.rect(self.screen, bg_color, iris_rect)

            granny_rect = pygame.Rect(self.SCREEN_WIDTH - 50 - self.PORTRAIT_WIDTH, self.portrait_y, self.PORTRAIT_WIDTH, self.PORTRAIT_HEIGHT)
            pygame.draw.rect(self.screen, bg_color, granny_rect)


    def draw_portrait(self, position):
        """Draw the portrait of the speaker based on position."""
        self.clear_portrait_area()  # First, clear both portrait areas
        self.portrait_y = self.SCREEN_HEIGHT - 170 - self.PORTRAIT_HEIGHT
        # Draw the new portrait based on the position of the speaker
        if position == "left":
            self.screen.blit(self.iris_portrait, (50, self.portrait_y))  # Draw Iris's portrait on the left
        elif position == "right":
            self.screen.blit(self.granny_portrait, (self.SCREEN_WIDTH - 50 - self.PORTRAIT_WIDTH, self.portrait_y))  # Draw Granny's portrait on the right

    # Function to wrap and render long text
    def wrap_text(self, text, font, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        return lines

    # Function to draw text box and current dialogue
    def draw_text_box(self, text):
        box_rect = pygame.Rect(50, self.SCREEN_HEIGHT - 150, self.SCREEN_WIDTH - 100, 100)
        pygame.draw.rect(self.screen, self.BOX_COLOR, box_rect)

        lines = self.wrap_text(text, self.FONT, box_rect.width - 2 * self.BOX_PADDING)

        y_offset = 0
        for line in lines:
            rendered_text = self.FONT.render(line, True, self.TEXT_COLOR)
            self.screen.blit(rendered_text, (box_rect.x + self.BOX_PADDING, box_rect.y + self.BOX_PADDING + y_offset))
            y_offset += self.FONT.get_linesize()
            
    def handle_npc_interaction():
        global quest_stage, item1_visible, item2_visible

        if quest_stage == 0:
            quest_stage = 1
            item1_visible = True
            return ("NPC: Oh dear! I lost my knitting yarn in the orchard...")


        elif quest_stage == 2:
            quest_stage = 3
            return ("NPC: Thank you, sweetpea! Now I can finish my scarf.")


        elif quest_stage == 3:
            quest_stage = 4
            item2_visible = True
            return ("NPC: Hmm... now I’ve lost my reading glasses in the garden...")


        elif quest_stage == 5:
            quest_stage = 6
            return("NPC: My glasses! You’re a star, darling. Thank you!")


        elif quest_stage in [1, 4]:
            return("NPC: Have you found what I asked for yet?")

        elif quest_stage == 6:
            return("NPC: That’s all for now. Go enjoy some tea under the rainbow.")


    # Game loop
    def is_finished(self):
        return self.finished
    
    def run(self):
        # Draw dialogue box and portrait only, leaving the background untouched
        if self.dialogue_index < len(self.dialogue):
            text = self.dialogue[self.dialogue_index]
            speaker = self.speakers[self.dialogue_index]  
            
            if speaker == "Iris":
                self.draw_portrait("left")  # Draw Iris's portrait on the left side
            elif speaker == "Granny":
                self.draw_portrait("right")  # Draw Granny's portrait on the right side

            self.draw_text_box(text)
            self.finished = False
        else:
            self.draw_text_box("The End. Thanks for playing!")
            self.finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Advance dialogue on spacebar press
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.dialogue_index < len(self.dialogue):
                    self.dialogue_index += 1
                # If player reads too fast and wants to reset
                if event.key == pygame.K_r:
                    self.dialogue_index = 0
                    self.finished = False

        pygame.display.flip()
