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

# Dialogue content
dialogue = [
    "Granny: \"Iris, honey...\"",
    "Granny: \"I want a pet butterfly.\"",
    "Granny: \"Can you find one for me?\"",
    "Iris: \"I've seen some in the garden!\"",
    "Iris: \"I'll catch the most beautiful one!\""
]
dialogue_index = 0

# Function to draw text box and current dialogue
def draw_text_box(text):
    # Draw box
    box_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 100)
    pygame.draw.rect(screen, BOX_COLOR, box_rect)
    
    # Draw text
    rendered_text = FONT.render(text, True, TEXT_COLOR)
    screen.blit(rendered_text, (box_rect.x + BOX_PADDING, box_rect.y + BOX_PADDING))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((100, 100, 255))  # Background color

    # Draw dialogue box
    if dialogue_index < len(dialogue):
        draw_text_box(dialogue[dialogue_index])
    else:
        draw_text_box("The End. Thanks for playing!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Advance dialogue on spacebar press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dialogue_index < len(dialogue):
                dialogue_index += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
