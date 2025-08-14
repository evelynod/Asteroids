import pygame               
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED 
from constants import PLAYER_SPEED

class Player(CircleShape):    
    def __init__(self, x, y):                  #  The Player constructor should take x and y integers as input, then:
        super().__init__(x,y,PLAYER_RADIUS)      # Call the parent class's constructor, also passing in PLAYER_RADIUS
        self.rotation = 0                           # Create a field called rotation, initialized to 0 (What is a field?)
        self.x = x                                  # Boots answered that a field is another name for instance variable, and needs self.--
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
        pygame.draw.polygon(screen, draw_color, triangle_points, line_width)  
        return       
    
    # Add a new method to the Player class called rotate.  It's going to take one argument: dt.
    # When it's called, it should add (PLAYER_TURN_SPEED * dt) to the player's current rotation.
    
    def rotate(self, dt):
        self.rotation = (PLAYER_TURN_SPEED * dt) + self.rotation
    
    # Paste in the following update method to the Player class:
    # Update the missing lines to call the rotate method with the dt argument.
    # To go left instead of right when a is pressed, 
    # you'll need to reverse dt... how can you do that...?

    # Hook the update method into the game loop by calling it on the player object each frame before rendering.
    #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVvv

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
           self.rotate(dt)     
        if keys[pygame.K_a]:          
           dt = -dt            
           self.rotate(dt)
        if keys[pygame.K_w]:                 
           self.move(dt)
        if keys[pygame.K_s]:
           dt = -dt
           self.move(dt)


    # Add a new method to the Player class called .move().  It takes one argument, dt.
    # We want to modify the player's position; but first, we need to do a little bit of math.
    # We start with a unit vector pointing straight up from (0, 0) to (0, 1).
    # We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
    # We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
    # Add the vector to our position to move the player.
    #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVv

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt