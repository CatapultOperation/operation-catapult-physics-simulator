import pygame
import os
import copy

from main.python.physicssim.graphics.GraphicalField import Direction
from main.python.physicssim.physics.staticfield import StaticField
from main.python.physicssim.menuItems.Size import Size
from main.python.physicssim.menuItems.Strength import Strength

class DraggableField:
	def __init__(self, pos, direction):
		"""Pos passed as list [x, y], direction as enum from GraphicsField file,
		width and height are size of object to be created"""
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

	def mouseCollision(self, event):
		if self.pos[0] < event.pos[0] < self.pos[0] + 40:
			if self.pos[1] < event.pos[1] < self.pos[1] + 40:
				return True
		return False

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
			power = 10000
		elif strength == Strength.MED:
			power = 16000
		else:
			power = 30000

		pos = copy.deepcopy(self.pos)
		newf = StaticField(pos, [pos[0]+width, pos[1]+height], power, self.direction)
		newf.graphicalObject.offSet = [pos[0], pos[1]]
		return newf
