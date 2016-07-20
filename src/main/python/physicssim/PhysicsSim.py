import pygame

import main.python.physicssim.graphics.GraphicsMain as graphics
from main.python.physicssim.graphics.GraphicalField import Direction
from main.python.physicssim.physics.particle import Particle
from main.python.physicssim.physics.staticfield import StaticField


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
particleList = []
fieldList = []

def tempInitLists():
	particleList.append(Particle([300, 300], 2, .01, 1/30))
	particleList.append(Particle([600, 700], 1, .01, 1/30))
	fieldList.append(StaticField([30, 30], [400, 400], 1000, Direction.EAST))

def update():
	for p in particleList:
		p.calculateDisplacement(particleList, fieldList)
	for p in particleList:
		p.finalizeValues()

	graphics.render(screen, particleList, fieldList)
	events = pygame.event.get()
	#concats lists because event handler doesn't need them in separate lists
	return graphics.events(screen, particleList, fieldList, events)

def mainLoop():
	while True:
		if update(): 
			return
		clock.tick(30)

tempInitLists()
mainLoop()