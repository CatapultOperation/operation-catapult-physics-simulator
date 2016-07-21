import pygame
import os

from main.python.physicssim.graphics.GraphicalField import Direction
from main.python.physicssim.physics.staticfield import StaticField
class DraggableField:
	def __init__(self, pos, direction, width, height):
		"""Pos passed as list [x, y], direction as enum from GraphicsField file,
		width and height are size of object to be created"""
		self.pos = pos
		self.direction = direction
		self.width = width
		self.height = height
		thisdir = os.path.dirname(__file__)
		self.dir = os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))

	def draw(self, screen):

		if self.direction == Direction.NORTH:
			pic = pygame.image.load(self.dir + "\\northfield.png")
		elif self.direction == Direction.EAST:
			pic = pygame.image.load(self.dir + "\\eastfield.png")
		elif self.direction == Direction.SOUTH:
			pic = pygame.image.load(self.dir + "\\southfield.png")
		else:
			pic = pygame.image.load(self.dir + "\\westfield.png")
		pic = pygame.transform.scale(pic, (40, 40))
		screen.blit(pic, self.pos)

	def getObject(self):
		"""Returns object to add to list for drawing"""
		return StaticField(self.pos, (self.pos[0]+self.width, self.pos[1]+self.height), 10000, self.direction)
