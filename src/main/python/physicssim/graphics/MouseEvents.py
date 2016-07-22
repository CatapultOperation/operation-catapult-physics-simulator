from math import *
import copy
from pygame import *



def handleEvents(screen, particleList, fieldList, draggables, events):
    quitState = False
    movingSomething = False

    for event in events:
        if event.type == QUIT:
            quitState = True

    for particle in particleList:
        for event in events:
            if event.type == MOUSEBUTTONDOWN: 
                particle.moveState = particle.graphicalObject.mouseCollision(event)
            
            elif event.type == MOUSEBUTTONUP: 
                particle.moveState = False
            
            if event.type == MOUSEMOTION: 
                if particle.moveState:
                    if not movingSomething: 
                        movingSomething = True
                        particle.velocity = (0.0, 0.0)
                        particle.pos[0] += event.rel[0]
                        particle.pos[1] += event.rel[1]
                        
    for field in fieldList:
        for event in events:
            if event.type == MOUSEBUTTONDOWN: 
                field.moveState = field.graphicalObject.mouseCollision(event)
            
            elif event.type == MOUSEBUTTONUP: 
                field.moveState = False
            
            if event.type == MOUSEMOTION: 
                if field.moveState:
                    if not movingSomething: 
                        movingSomething = True
                        field.topLeft[0] += event.rel[0]
                        field.topLeft[1] += event.rel[1]
                        field.bottomRight[0] += event.rel[0]
                        field.bottomRight[1] += event.rel[1]

    dragToAdd = None
    for draggable in draggables:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                draggable.moveState = draggable.mouseCollision(event)
                if draggable.moveState:
                    dragToAdd = copy.deepcopy(draggable)
                    dragToAdd.moveState = False

            elif event.type == MOUSEBUTTONUP:
                #TODO: make object using ui selections, then remove current draggable from draggables list.
                draggable.moveState = False
                break #gets out of loop so that removed draggable is not used in the rest of the loop

            if event.type == MOUSEMOTION:
                if draggable.moveState:
                    if not movingSomething:
                        movingSomething = True
                        draggable.pos[0] += event.rel[0]
                        draggable.pos[1] += event.rel[1]
    if dragToAdd is not None:
        draggables.append(dragToAdd)

                    
    return quitState