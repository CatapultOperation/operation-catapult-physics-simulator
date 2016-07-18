from math import *

import pygame
from pygame.locals import *

from MouseEvents import *
from GraphicalParticle import GraphicalParticle


def render(screen, objects):
    screen.fill((255, 255, 255))
    
    for object in objects: 
        pygame.draw.circle(screen, object.color, object.center, object.radius)
    
    pygame.display.flip()

def events(screen, objects, events):
    mouse.events(screen, objects, events)