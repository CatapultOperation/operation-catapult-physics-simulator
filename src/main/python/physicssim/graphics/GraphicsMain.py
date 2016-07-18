from math import *

import pygame
from pygame.locals import *

from src.main.python.physicssim.graphics.GraphicalParticle import GraphicalParticle
from src.main.python.physicssim.graphics.GraphicalField import GraphicalField
import src.main.python.physicssim.graphics.MouseEvents as eventHandler


def render(screen, objects):
    screen.fill((255, 255, 255))
    
    for obj in objects:
        obj.update()
        obj.draw()
    
    pygame.display.flip()

def events(screen, objects, events):
    eventHandler.handleEvents(screen, objects, events)