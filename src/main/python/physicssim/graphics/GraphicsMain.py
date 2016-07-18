from math import *

import pygame
from pygame.locals import *

import MouseEvents as mouse


def render(screen, objects):
    screen.fill((255, 255, 255))
    
    for object in objects: 
        object.update()
        object.draw()
    
    pygame.display.flip()

def events(screen, objects, events):
    mouse.events(screen, objects, events)