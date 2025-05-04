import pygame
import sys


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
            "Granny: \"Iris, my dear...\"",
            "Granny: \"Can you please bring me a cup of tea?\"",
            "Iris: \"Of course, Granny!\""
        ]
        self.dialogue_index = 0
        self.screen = screen  # Keep track of the screen passed from main

    # Function to draw text box and current dialogue
    def draw_text_box(self, text):
        # Draw box
        box_rect = pygame.Rect(50, self.SCREEN_HEIGHT - 150, self.SCREEN_WIDTH - 100, 100)
        pygame.draw.rect(self.screen, self.BOX_COLOR, box_rect)
        
        # Draw text
        rendered_text = self.FONT.render(text, True, self.TEXT_COLOR)
        self.screen.blit(rendered_text, (box_rect.x + self.BOX_PADDING, box_rect.y + self.BOX_PADDING))

    # Game loop
    def is_finished(self):
        return self.finished
    
    def run(self):

        # Draw dialogue box
        if self.dialogue_index < len(self.dialogue):
            self.draw_text_box(self.dialogue[self.dialogue_index])
            self.finished = False
        else:
            self.draw_text_box("")
            self.finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Advance dialogue on spacebar press
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.dialogue_index < len(self.dialogue):
                    self.dialogue_index += 1
                    # If player reads to fast and wants to reset
                if event.key == pygame.K_r:
                    self.dialogue_index = 0
                    self.finished = False

        pygame.display.flip()