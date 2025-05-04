from assets import *

class Sound:

    def GrannyYap():
        yap = pygame.mixer.Sound(ANIMALYAP)
        pygame.mixer.Sound.play(yap)

    def footstep():
        step = pygame.mixer.Sound(STEPSOUND)
        pygame.mixer.Sound.play(step)

    def paused():
        pygame.mixer.music.pause()


    def unpause():
        global pause

        pygame.mixer.music.unpause()

        pause = False
