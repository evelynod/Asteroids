# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #2.12




def main():
    pygame.init()   # I'm not sure if the () should have anything in it.  Possibly (numpass, numfail)2-12
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()   # Add pygame.time.Clock object and set an instance variable.
    dt = 0                # delta-time --The time passed since last frame was drawn

    # In your main function, instantiate a Player object.
    #  You can pass these values to the constructor 
    # to spawn it in the middle of the screen:

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)



    running = True
    while running:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return  # This will break the loop safely  Boot's suggested "running == False"

        dt = (clock.tick(60))/1000                # pause the loop until 1/60 second has passed  
        screen.fill((0, 0, 0))     # Fill the screen with black
        player.update(dt)
        player.draw(screen)
       
        pygame.display.flip()      # Update the display
       


    pygame.quit()


if __name__ == "__main__":
    main()
