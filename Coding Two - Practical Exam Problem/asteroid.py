from turtle import update
import pygame
import numpy as np
import math
import random


clock = pygame.time.Clock()
 







class Asteroid:
    def __init__(self, x, y, radius, surface, velocity, upordown , outsidevector, maptocanvas):
        # Position of the tip of the asteroid
        
        self.pos = np.array([x, y])
       
        self.outsidevector = outsidevector
        self.maptocanvas = maptocanvas
       
        # Additional properties goes here:
    
        self.upordown = upordown

        self.velocity = velocity

        # Leave the rest of these properties
        self.surface = surface
        self.radius = radius

    def update(self, asteroids):
        # Action required!
        
        #randomize initial position on screen

       
        

        upordown = random.randrange(0, 2)
        #print( upordown)

       # get random vector point
        # i have this which is 0 to 1 and this

        print(self.outsidevector)
        #print ( "[", self.outsidevector, "," , self.outsidevector, "]" )
       # self.outsidevector = (((self.outsidevector - 0.1) * self.maptocanvas) / self.outsidevector) + 1
        
       # print(self.outsidevector)
        #self.outside vector gives me <map object at 0x11a536a00>
        #now i want to convert map object into vector
        

       # print ( self.outsidevector)
        

      # make vector initial position move to random vector point

      #  self.pos = self.pos *  self.outsidevector
        
      #move to  outsidevector


       # move circle to random vector
       
        #if upordown == 1: 
       #     self.pos[0] = self.pos[0] -1
        #    self.pos[1] = self.pos[1] +1
        #elif  upordown == 0: 
         #   self.pos[0] = self.pos[0] +1
         #   self.pos[1] = self.pos[1] -1
        


        #self.pos += random.randrange(0, self.surface.get_height())
        
        #move around x and y with vector
       
       
        # Set position of asteroid based on given parameter
        #self.pos  = self.pos
        
        

        # Leave the rest of the code
        # Wrap asteroid around the edges so it always stay on screen
        if self.pos[0] > self.surface.get_width():
            self.pos[0] = 0
            self.pos[0]
        elif self.pos[0] < 0:
            self.pos[0] = self.surface.get_width()

        if self.pos[1] > self.surface.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = self.surface.get_height()






    # Draw the asteroid onto the canvas
    def draw(self):
        clock.tick(30)

        
        
        #self.pos += self.velocity 
        
        #mag = pygame.math.Vector2.magnitude(self.pos)


        
        pygame.draw.circle(self.surface, (0, 0, 255), (self.pos[0]  ,self.pos[1] ), self.radius)

        






clock.tick(60) 