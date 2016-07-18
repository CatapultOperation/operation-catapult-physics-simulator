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
	#TODO: go through each element in both lists and draw them

	pygame.display.flip()

def events(screen, objects, events):
	eventHandler.handleEvents(screen, objects, events)