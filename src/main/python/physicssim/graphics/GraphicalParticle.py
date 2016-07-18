from enum import Enum
from math import sqrt

import pygame



class Charge(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class GraphicalParticle:
    def __init__(self, center, radius, charge, color=(0, 0, 0)):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color
        
    def update(self, center, radius):
        self.center = center
        self.radius = radius
        
    def draw(self, screen, position):
        particleSurface = pygame.Surface(self.radius * 2, self.radius * 2)
        pygame.draw.circle(particleSurface, self.color, self.center, self.radius)
        screen.blit(particleSurface, (position[0] - self.radius, position[1] - self.radius))
        
    def mouseCollision(self, event):
         mouseDistance = sqrt((event.pos[0] - object.center[0]) ** 2 + (event.pos[1] - object.center[1]) ** 2)
         return mouseDistance <= self.radius