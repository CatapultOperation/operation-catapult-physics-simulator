from math import *

import pygame
from pygame.locals import *
import main.python.physicssim.graphics.MouseEvents as eventHandler
from main.python.physicssim.graphics.GraphicalField import GraphicalField


def render(screen, particleList, fieldList, draggables):
	"""Takes as arguments screen (pygame screen), particleList (list of physical particles),
	and fieldList (list of physical fields"""
	screen.fill((255, 255, 255))
	for f in fieldList:
		f.draw(screen)
	for p in particleList:
		p.draw(screen)
	for d in draggables:
		d.draw(screen)


	pygame.display.flip()

def events(screen, particleList, fieldList, draggables, events):
	return eventHandler.handleEvents(screen, particleList, fieldList, draggables, events)