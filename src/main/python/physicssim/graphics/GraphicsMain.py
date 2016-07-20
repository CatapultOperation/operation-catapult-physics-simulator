from math import *

import pygame
from pygame.locals import *

from src.main.python.physicssim.graphics.GraphicalParticle import GraphicalParticle
from src.main.python.physicssim.graphics.GraphicalField import GraphicalField
import src.main.python.physicssim.graphics.MouseEvents as eventHandler


def render(screen, particleList, fieldList):
	"""Takes as arguments screen (pygame screen), particleList (list of physical particles),
	and fieldList (list of physical fields"""
	screen.fill((255, 255, 255))

	for f in fieldList:
		f.draw(screen)
	for p in particleList:
		p.draw(screen)

	pygame.display.flip()

def events(screen, objects, events):
	eventHandler.handleEvents(screen, objects, events)