import pygame

import src.main.python.physicssim.graphics.GraphicsMain as graphics
from src.main.python.physicssim.physics.particle import Particle
from src.main.python.physicssim.physics.staticfield import StaticField
from src.main.python.physicssim.graphics.GraphicalField import Direction


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
particleList = []
fieldList = []

def tempInitLists():
	pass
	particleList.append(Particle((200, 200), 2, 1, 1/30))
	particleList.append(Particle((600, 600), 1, -1, 1/30))
	#fieldList.append(StaticField((120, 30), (180, 160), 1, Direction.EAST))

def update():
	for p in particleList:
		p.calculateDisplacement(particleList, fieldList)
	for p in particleList:
		p.finalizeValues()

	graphics.render(screen, particleList, fieldList)
	events = pygame.event.get()
	#concats lists because event handler doesn't need them in separate lists
	graphics.events(screen, particleList + fieldList, events)

def mainLoop():
	while True:
		update()
		clock.tick(30)

tempInitLists()
mainLoop()