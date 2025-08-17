import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS





class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, (150, 150, 255), self.position, SHOT_RADIUS, 2)   # Not sure if I want the line-width 2 here.)