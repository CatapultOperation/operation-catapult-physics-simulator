import pygame
import os

from main.python.physicssim.graphics.GraphicalField import Direction
from main.python.physicssim.physics.staticfield import StaticField
from main.python.physicssim.menuItems.Size import Size
from main.python.physicssim.menuItems.Strength import Strength

class DraggableField:
	def __init__(self, pos, direction):
		"""Pos passed as list [x, y], direction as enum from GraphicsField file,
		width and height are size of object to be created"""
		self.moveState = False
		self.pos = pos
		self.direction = direction
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
		pic.set_colorkey((255, 255, 255))
		screen.blit(pic, self.pos)

	def getObject(self, size, strength):
		"""Returns object to add to list for drawing;
		pass size as Size enum, pass strength as Strength enum"""
		if size == Size.SMALL:
			width = 150
			height = 150
		elif size == Size.MED:
			width = 250
			height = 250
		else:
			width = 400
			height = 400

		if strength == Strength.LOW:
			power = 6000
		elif strength == Strength.MED:
			power = 12000
		else:
			power = 20000

		return StaticField(self.pos, (self.pos[0]+width, self.pos[1]+height), power, self.direction)
