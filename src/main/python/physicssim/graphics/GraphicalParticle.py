from enum import Enum
from math import sqrt
import os

import pygame


class Charge(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class GraphicalParticle:
    def __init__(self, center, radius, charge, color=(255, 0, 0)):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color
        thisdir = os.path.dirname(__file__)
        self.dir = os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))
        
    def update(self, center, radius, charge, color=(255, 0, 0)):
        self.center = center
        self.radius = radius
        self.charge = charge
        self.color = color

    def draw(self, screen):
        if self.charge == Charge.NEGATIVE:
            pic = pygame.image.load(self.dir + "\\negativeparticle.png")
        else:
            pic = pygame.image.load(self.dir + "\\positiveparticle.png")
        pic = pygame.transform.scale(pic, (self.radius*2, self.radius*2))
        pic.set_colorkey((255, 255, 255))
        screen.blit(pic, (self.center[0]-self.radius, self.center[1]-self.radius))
        
    def mouseCollision(self, event):
        mouseDistance = sqrt((event.pos[0] - self.center[0]) ** 2 + (event.pos[1] - self.center[1]) ** 2)
        return mouseDistance <= self.radius