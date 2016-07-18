from math import *

import pygame
from pygame.locals import *

import mouseEvents as mouse


def render(screen, objects):
    screen.fill((0, 0, 0))
    
    for object in objects: 
        pygame.draw.circle(screen, object.color, object.center, object.radius)
    
    pygame.display.flip()

def events(screen, objects, events):
    mouse.events(screen, objects, events)