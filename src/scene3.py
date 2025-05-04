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
# Dialogue content and who is speaking (left or right)
dialogue = [
    "Iris, honey... I am planning to make apple cake. We will need the reddest of apples!",
    "I'll get them in the garden!"
]

speakers = [
    "Granny",
    "Iris"
    "Iris, honey... I am planning to make apple cake. We will need the reddest of apples!",
    "I'll get them in the garden!"
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

# Portrait size and position logic
PORTRAIT_WIDTH = 120
PORTRAIT_HEIGHT = 160
PORTRAIT_COLOR = (255, 182, 193) 

def draw_portrait(position):
    if position == "left":
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

    lines = wrap_text(text, FONT, box_rect.width - 2 * BOX_PADDING)

    y_offset = 0
    for line in lines:
        rendered_text = FONT.render(line, True, TEXT_COLOR)
        screen.blit(rendered_text, (box_rect.x + BOX_PADDING, box_rect.y + BOX_PADDING + y_offset))
        y_offset += FONT.get_linesize()

# Game loop
clock = pygame.time.Clock()
dialogue_index = 0
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