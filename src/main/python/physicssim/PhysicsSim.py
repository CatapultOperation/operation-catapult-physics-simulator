import pygame
import os

import main.python.physicssim.graphics.GraphicsMain as graphics
from main.python.physicssim.graphics.GraphicalField import Direction,GraphicalField
from main.python.physicssim.physics.particle import Particle
from main.python.physicssim.physics.staticfield import StaticField
from main.python.physicssim.menuItems.draggableField import DraggableField
from main.python.physicssim.menuItems.draggableParticle import DraggableParticle
from main.python.physicssim.graphics.GraphicalParticle import Charge
from main.python.physicssim.graphics.GraphicalUI import GraphicalUI


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
particleList = []
fieldList = []
draggables = []
graphUi = GraphicalUI()


def makeDraggables():
	draggables.clear()
	draggables.append(DraggableParticle([10, 10], Charge.POSITIVE))
	draggables.append(DraggableParticle([10, 60], Charge.NEGATIVE))
	draggables.append(DraggableField([10, 110], Direction.NORTH))
	draggables.append(DraggableField([10, 160], Direction.EAST))
	draggables.append(DraggableField([10, 210], Direction.SOUTH))
	draggables.append(DraggableField([10, 260], Direction.WEST))


def tempInitLists():
	pass
	particleList.append(Particle([400, 400], 2, -.01, 1/30))
	particleList.append(Particle([300, 300], 2, .01, 1/30))
	particleList.append(Particle([600, 700], 1, .01, 1/30))
	fieldList.append(StaticField([50, 50], [600, 600], 10000, Direction.NORTH))

def update():
	for p in particleList:
		p.calculateDisplacement(particleList, fieldList)
	for p in particleList:
		p.finalizeValues()

	graphics.render(screen, particleList, fieldList, draggables, graphUi)
	events = pygame.event.get()
	
	#concats lists because event handler doesn't need them in separate lists
	return graphics.events(screen, particleList, fieldList, draggables, graphUi, events)

def mainLoop():
	while True:
		if update(): 
			return
		clock.tick(30)

makeDraggables()
#tempInitLists()
mainLoop()