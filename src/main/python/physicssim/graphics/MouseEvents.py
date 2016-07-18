from math import *

from pygame import *
import GraphicalParticle
import GraphicalField


def events(screen, objects, events):
    
    for object in objects:
        for event in events: 
            if event.type == QUIT: 
                return
            
            if event.type == MOUSEBUTTONDOWN: 
                movestate = object.mouseColision(event)
            
            if event.type == MOUSEBUTTONUP: 
                moveState = False
            
            if event.type == MOUSEMOTION: 
                if moveState: 
                    if object.instanceof(GraphicalParticle):
                        object.center[0] += event.rel[0]
                        object.center[1] += event.rel[1]
                    elif object.instanceof(GraphicalField): 
                        object.rect.move(event.rel)