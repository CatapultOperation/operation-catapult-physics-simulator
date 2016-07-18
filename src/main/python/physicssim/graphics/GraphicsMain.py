from math import *

import pygame
from pygame.locals import *

<<<<<<< HEAD
from MouseEvents import *
from GraphicalParticle import GraphicalParticle
=======
import MouseEvents as mouse
>>>>>>> 466e371c83dfa0ba164515d6446e7e569266457b


def render(screen, objects):
    screen.fill((255, 255, 255))
    
    for object in objects: 
        object.update()
        object.draw()
    
    pygame.display.flip()

def events(screen, objects, events):
    mouse.events(screen, objects, events)