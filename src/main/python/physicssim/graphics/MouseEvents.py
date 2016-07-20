from math import *

from pygame import *

from main.python.physicssim.graphics import GraphicalParticle, GraphicalField
from main.python.physicssim.physics.particle import Particle
from main.python.physicssim.physics.staticfield import StaticField


def handleEvents(screen, particleList, fieldList, events):
    quitState = False
    movingSomething = False

    for particle in particleList:
        for event in events: 
            if event.type == QUIT:
                quitState = True

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
            if event.type == QUIT:
                quitState = True

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
                    
    return quitState