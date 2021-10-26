import pygame
from pygame import constants
from pygame.constants import K_ESCAPE, KEYDOWN
import constants

# Game window
pygame.display.set_caption('Scrolling Platformer')


class Main():
    def __init__(self):
        # Frames
        self.clock = pygame.time.Clock()
        self.frames_per_second = 60

        # Game variables

    def run(self):
        running = True

        # Game loop
        while running == True:

            # Game frames per second
            self.clock.tick(self.frames_per_second)

            # Exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Escape key
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return

            # Game window
            constants.SCREEN.fill(constants.CYAN)

            # Display the screen
            pygame.display.flip()


# Run only main class
if __name__ == '__main__':
    Main().run()
