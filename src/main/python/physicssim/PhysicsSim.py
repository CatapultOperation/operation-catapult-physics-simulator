import pygame

import src.main.python.physicssim.graphics.GraphicsMain as graphics


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
particleList = []
fieldList = []

#TODO: put a graphics type object into each physical type object and handle updating between them

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


