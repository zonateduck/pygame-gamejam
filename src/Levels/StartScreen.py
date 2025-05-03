import pygame
import sys
pygame.font.init()

class StartScreen:
    def __init__(self):
        self.LIGHT_BLUE = (200, 200, 255)
        self.box_size = 500

        self.font = pygame.font.SysFont(None, 48)
        self.text_headline = self.font.render("Color Quest", True, (0, 0, 0))
        self.text_space = self.font.render("Press Space to continue", True, (0, 0, 0))

    def enter(self):
        pass

    def run(self, screen):        
        width, height = screen.get_size()
        pygame.draw.rect(screen, self.LIGHT_BLUE, (0, 0, width, height))
        screen.blit(self.text_headline, (200, 200))
        screen.blit(self.text_space, (200, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

    def exit(self):
        pass