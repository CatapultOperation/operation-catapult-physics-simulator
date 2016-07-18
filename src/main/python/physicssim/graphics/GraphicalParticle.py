from enum import Enum

import pygame


class Charge(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class MyClass(object):

    
    def __init__(self, center, radius, charge, color=(0, 0, 0)):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color
        
    def update(self, position, radius):
        self.center = position
        self.radius = radius
        
    def draw(self, screen, position):
        particleSurface = pygame.Surface(self.radius * 2, self.radius * 2)
        pygame.draw.circle(self.particleSurface, self.color, self.center, self.radius)
        screen.blit(self.particleSurface, (position[0] - self.radius, position[1] - self.radius))