import pygame

pygame.init()
pygame.mixer.init()

class Music:
    def __init__(self, music_file):
        self.music_file = music_file

    def play(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)

# --- Main Game Code ---
# Create a window (optional but useful to keep the window open)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Example")

# Play music
bg_music = Music("lydfilnavn.mp3")
bg_music.play()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
