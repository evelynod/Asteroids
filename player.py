import pygame                # Not sure if I need this.  Hello, Boots?  I hope you are having a nice day.  Do I need import pygame?
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):    
    def __init__(self, x, y):                  #  The Player constructor should take x and y integers as input, then:
        super().__init(x,y,PLAYER_RADIUS)      # Call the parent class's constructor, also passing in PLAYER_RADIUS
        self.rotation = 0                           # Create a field called rotation, initialized to 0 (What is a field?)
        self.x = x
        self.y = y


    def triangle(self):                        # triangle method pasted into Player class 

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #To draw the player, override the draw method of CircleShape.  That means you don't use super().
    # It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
    # 
    # A color (use "white")
    #A list of points (use self.triangle() that we provided for you)
    #A line width (use 2)



    #draw_color = "white"
    def draw(self, screen ):
        draw_color = "white"
        triangle_points = self.triangle()
        line_width = 2
        screen.pygame.draw.polygon(screen, draw_color, triangle_points, line_width)  

        # At present, I'm not sure what to do here.
        return       