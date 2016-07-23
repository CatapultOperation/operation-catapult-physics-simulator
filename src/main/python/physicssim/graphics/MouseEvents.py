from math import *
import pygame
from pygame import *
from main.python.physicssim.menuItems.draggableParticle import DraggableParticle
from main.python.physicssim.menuItems.draggableField import DraggableField


def handleEvents(screen, particleList, fieldList, draggables, graphUi, events):
    quitState = False
    movingSomething = False

    for event in events:
        if event.type == QUIT:
            quitState = True
        elif event.type == MOUSEBUTTONDOWN:
            graphUi.mouseCollision(event)

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
                    else:
                        particle.moveState = False

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
                    else:
                        field.moveState = False

    for draggable in draggables:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if draggable.mouseCollision(event):
                    if isinstance(draggable, DraggableParticle):
                        newPart = draggable.getObject(graphUi.size, graphUi.strength, 1/30)
                        newPart.moveState = True
                        particleList.append(newPart)
                    else:
                        newField = draggable.getObject(graphUi.size, graphUi.strength)
                        newField.moveState = True
                        fieldList.append(newField)

                    
    return quitState