from math import *

from pygame import *


def events(screen, objects, events):
    
    for object in objects:
        for event in events: 
            if event.type == QUIT: 
                return
            
            if event.type == MOUSEBUTTONDOWN: 
                mouseDistance = sqrt((event.pos[0] - object.center[0]) ** 2 + (event.pos[1] - object.center[1]) ** 2)
                
                if mouseDistance <= object.radius: 
                    moveState = True
            
            if event.type == MOUSEBUTTONUP: 
                moveState = False
            
            if event.type == MOUSEMOTION: 
                if moveState: 
                    object.center[0] += event.rel[0]
                    object.center[1] += event.rel[1]