import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meowgical Visual Novel")

# Fonts
FONT = pygame.font.SysFont("lucida console", 24)
TEXT_COLOR = (255, 255, 255)
BOX_COLOR = (0, 0, 0)
BOX_PADDING = 20

# Dialogue content and who is speaking (left or right)
dialogue = [
    "Iris, my dear... Can you please bring me a cup of tea?",
    "Of course, Granny!"
]

speakers = [
    "Granny",
    "Iris"
]

# Portrait size and position logic
PORTRAIT_WIDTH = 120
PORTRAIT_HEIGHT = 160
PORTRAIT_COLOR = (255, 182, 193) 

def draw_portrait(position):
    if position == "left":
        # TODO: the rectangles should be replaced with character portraits, 
        # left is always Iris, right is either empty or Granny
        rect = pygame.Rect(50, 300, PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
    elif position == "right":
        rect = pygame.Rect(SCREEN_WIDTH - 50 - PORTRAIT_WIDTH, 300, PORTRAIT_WIDTH, PORTRAIT_HEIGHT)
    pygame.draw.rect(screen, PORTRAIT_COLOR, rect)

# Function to wrap and render long text
def wrap_text(text, font, max_width):
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
def draw_text_box(text):
    box_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 100)
    pygame.draw.rect(screen, BOX_COLOR, box_rect)

    lines = wrap_text(text, FONT, box_rect.width - 2 * BOX_PADDING)

    y_offset = 0
    for line in lines:
        rendered_text = FONT.render(line, True, TEXT_COLOR)
        screen.blit(rendered_text, (box_rect.x + BOX_PADDING, box_rect.y + BOX_PADDING + y_offset))
        y_offset += FONT.get_linesize()

# Game loop
clock = pygame.time.Clock()
dialogue_index = 0
running = True
while running:
    screen.fill((100, 100, 255))  # Background color

    if dialogue_index < len(dialogue):
        text = dialogue[dialogue_index]
        speaker = speakers[dialogue_index]

        if speaker == "Iris":
            draw_portrait("left")
        else:
            draw_portrait("right")

        draw_text_box(text)
    else:
        draw_text_box("The End. Thanks for playing!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dialogue_index < len(dialogue):
                dialogue_index += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
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