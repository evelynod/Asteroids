# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #2.12




def main():
    pygame.init()   # I'm not sure if the () should have anything in it.  Possibly (numpass, numfail)2-12
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()   # Add pygame.time.Clock object and set an instance variable.
    dt = 0                # delta-time --The time passed since last frame was drawn




    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # This will break the loop safely  Boot's suggested "running == False"

        dt = (clock.tick(60))/1000                # pause the loop until 1/60 second has passed  
        screen.fill((0, 0, 0))     # Fill the screen with black
        pygame.display.flip()      # Update the display


    pygame.quit()


if __name__ == "__main__":
    main()
