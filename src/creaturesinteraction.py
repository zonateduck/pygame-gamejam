import pygame

# Not used for the moment
show_prompt = False # Flag to decide whether to draw the prompt

# called specifically when interacting with the cat
def draw_cat_interaction(screen, text="meow :3"):
    font = pygame.font.SysFont(None, 50)
    color = (255, 255, 255)
    bg_color = (0,0,0)
    padding = 10


    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() - 100)


    # Draw background box behind the text
    bg_rect = text_rect.inflate(padding * 2, padding * 2)
    pygame.draw.rect(screen, bg_color, bg_rect, border_radius=10)

    # Draw text
    screen.blit(text_surface, text_rect)

# called specifically when interacting with tu-tor
def draw_tutor_interaction(screen, text="it's tu-tor, from sonen!"):
    font = pygame.font.SysFont(None, 50)
    color = (255, 255, 255)
    bg_color = (0,0,0)
    padding = 10


    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() - 100)


    # Draw background box behind the text
    bg_rect = text_rect.inflate(padding * 2, padding * 2)
    pygame.draw.rect(screen, bg_color, bg_rect, border_radius=10)

    # Draw text
    screen.blit(text_surface, text_rect)