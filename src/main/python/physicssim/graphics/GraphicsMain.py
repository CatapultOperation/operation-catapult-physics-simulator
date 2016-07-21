from math import *

import pygame
from pygame.locals import *
import main.python.physicssim.graphics.MouseEvents as eventHandler
from main.python.physicssim.graphics.GraphicalField import GraphicalField


def render(screen, particleList, fieldList):
	"""Takes as arguments screen (pygame screen), particleList (list of physical particles),
	and fieldList (list of physical fields"""
	screen.fill((255, 255, 255))

	for field in fieldList:
		field.draw(screen)
	for particle in particleList:
		particle.draw(screen)

	pygame.display.flip()

def events(screen, particleList, fieldList, events):
	return eventHandler.handleEvents(screen, particleList, fieldList, events)