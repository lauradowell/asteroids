import pygame
import numpy as np
import math
import utils

class Ship:
    def __init__(self, x, y, surface):
        # Position of the tip of the ship
        self.pos = np.array([x, y])
        # Rotation angle of the ship relative to the tip of the ship
        self.angle = 0.0
        # Additional properties goes here:


        # Leave the rest of these properties
        self.surface = surface
        self.radius = 20
        self.color = (0, 0, 0)
        self.collided = False

    # Update properties of the ship
    def update(self, mouse_pos, asteroids, game_status):
        # Action required!
        
        #calculate distance between mouse and ship
        dist = np.linalg.norm(mouse_pos-self.pos)
        self.mouse_pos = np.array(pygame.mouse.get_pos(), dtype=float)
       
        # Set position of ship based on given parameter
        

        # Determine rotation angle of ship to point at cursor
        #self.angle = self.angle
        

        unit_vector_1 = self.pos / np.linalg.norm(self.pos)
        unit_vector_2 = self.mouse_pos / np.linalg.norm(self.mouse_pos)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        self.angle = np.arccos(dot_product)





        

        # Leave the rest of the code
        # Check for collision
        if game_status == "started":
            self.collision(asteroids, game_status)

    # Draw the ship onto the canvas
    def draw(self):

        

        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    # Detect whether ship has collided with an asteroid
    def collision(self, asteroids, game_status):
        for asteroid in asteroids:
            if np.linalg.norm(asteroid.pos - self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 0, 0)
                self.collided = True
                break



