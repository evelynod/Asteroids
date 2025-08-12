


class Player(CircleShape):    
    def __init__(self, x, y):                  #  The Player constructor should take x and y integers as input, then:
        super().__init(x,y,PLAYER_RADIUS)      # Call the parent class's constructor, also passing in PLAYER_RADIUS
        rotation = 0                           # Create a field called rotation, initialized to 0 (What is a field?)

        
    def triangle(self):                        # triangle method pasted into Player class 

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]