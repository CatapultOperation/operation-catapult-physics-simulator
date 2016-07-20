import math

from main.python.physicssim.graphics.GraphicalField import Direction, \
	GraphicalField


class StaticField:
	def __init__(self, topLeft, bottomRight, strength, cardinalDirection):
		"""Takes arguments topLeft as list [x, y], bottomRight as list [x, y], strength (in N/C),
		and cardinalDirection as an enum from GraphicalField"""
		self.moveState = False
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.strength = strength
		self.cardinalDirection = cardinalDirection
		if cardinalDirection == Direction.NORTH:
			self.direction = math.pi/2
		elif cardinalDirection == Direction.EAST:
			self.direction = 0
		elif cardinalDirection == Direction.SOUTH:
			self.direction = 3*math.pi/2
		elif self.cardinalDirection == Direction.WEST:
			self.direction = math.pi
		self.graphicalObject = GraphicalField(topLeft, bottomRight, self.cardinalDirection, self.strength)

	def getTopLeft(self):
		"""returns top left coordinate of field as tuple (x, y)"""
		return self.topLeft

	def getBottomRight(self):
		"""returns bottom right coordinate of field as tuple (x, y)"""
		return self.bottomRight

	def getStrength(self):
		"""returns strength of field (in N/C)"""
		return self.strength

	def getDirection(self):
		"""returns direction of field in radians"""
		return self.direction

	def draw(self, screen):
		"""Draws object by using GraphicalField object, takes pygame screen as argument"""
		self.graphicalObject.draw(screen)