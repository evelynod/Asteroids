import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS 



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        


    def draw(self, screen):
       
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)       
        return


    #Override the update() method so that it moves
    #  in a straight line at constant speed.
    # On each frame, it should add (self.velocity * dt)
    #  to its position (get self.velocity from its parent class, CircleShape).



    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        return
    
    def split(self):
        self.kill()         # Asteroid should immediately .kill() itself
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            random_angle = random.uniform(20,50)    # Generate a random angle 20-50 degrees
            self.velocity_new = self.velocity.rotate(random_angle)
            self.velocity_new_inv = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS      # Now we have smaller asteroids.  Here are their radii.
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)     # Create two new Asteroid objects at the current asteroid position with the new radius.
            mult1 = random.uniform(1.1, 1.5)                             # Give each new asteroid its own random speed
            mult2 = random.uniform(1.1, 1.5)
            new_asteroid_1.velocity = self.velocity.rotate(random_angle) * mult1
            new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * mult2


            



