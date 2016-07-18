import pygame

import src.main.python.physicssim.graphics.GraphicsMain as graphics


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
objects = []

def update():
	events = pygame.event.get()

	graphics.events(screen, objects, events)

def mainLoop():
	while True:
		update()
		clock.tick(30)
