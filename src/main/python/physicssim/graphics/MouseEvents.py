from math import *

from pygame import *
from src.main.python.physicssim.graphics.GraphicalParticle import GraphicalParticle
from src.main.python.physicssim.graphics.GraphicalField import GraphicalField


def handleEvents(screen, objects, events):
    
    for obj in objects:
        for event in events: 
            if event.type == QUIT: 
                return
            
            if event.type == MOUSEBUTTONDOWN: 
                movestate = obj.mouseCollision(event)
            
            if event.type == MOUSEBUTTONUP: 
                moveState = False
            
            if event.type == MOUSEMOTION: 
                if moveState: 
                    if obj.instanceof(GraphicalParticle):
                        obj.center[0] += event.rel[0]
                        obj.center[1] += event.rel[1]
                    elif obj.instanceof(GraphicalField):
                        obj.rect.move(event.rel)