from enum import Enum

from pygame import surface
import pygame

class Direction(Enum):
	NORTH = 1
	EAST = 2
	SOUTH = 3
	WEST = 4

class GraphicalField:
	def __init__(self, topLeft, bottomRight, direction, strength, color=(0, 0, 255)):
		self.spacing = strength
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.rect = pygame.Rect(topLeft, (bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]))
		self.direction = direction
		self.color = color
		self.initArrows()

	def update(self, topLeft, bottomRight, direction, strength, color=(0, 0, 255)):
		self.spacing = strength
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.rect = pygame.Rect(topLeft, (bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]))
		self.direction = direction
		self.spacing = strength
		self.color = color
		self.initArrows()

	def draw(self, screen):
		rectSurface = pygame.Surface((self.rect.width, self.rect.height))
		rectSurface.fill((255, 255, 255))
		self.drawArrow(rectSurface)
		pygame.draw.rect(rectSurface, self.color, self.rect, 10)
		screen.blit(rectSurface, self.topLeft)

	def mouseCollision(self, event):
		return self.rect.collidepoint(event.pos()[0], event.pos()[1])

	def initArrows(self):
		self.arrowEast = pygame.Surface((30, 10))
		self.arrowEast.fill((255, 255, 255))
		pygame.draw.line(self.arrowEast, (0, 0, 0), (2, 5), (28, 5), 1)
		pygame.draw.line(self.arrowEast, (0, 0, 0), (28, 5), (22, 2), 1)
		pygame.draw.line(self.arrowEast, (0, 0, 0), (28, 5), (22, 8), 1)
		self.arrowNorth = pygame.transform.rotate(self.arrowEast, -90)
		self.arrowSouth = pygame.transform.rotate(self.arrowEast, 90)
		self.arrowWest = pygame.transform.rotate(self.arrowEast, 180)

	def drawArrow(self, screen):
		self.transformArrows()

		if self.direction == Direction.NORTH:
			remainder = self.rect.width() % (self.arrowEast.get_width() + self.spacing)
			for i in (0, (self.rect.width() // (self.arrowEast.get_width() + self.spacing)) - 1):
				screen.blit(self.arrowNorth, ((remainder / 2) + i * (self.arrowEast.get_width() + self.spacing), 3))

		elif self.direction == Direction.SOUTH:
			remainder = self.rect.width % (self.arrowEast.get_width() + self.spacing)
			for i in (0, (self.rect.width // (self.arrowEast.get_width() + self.spacing)) - 1):
				screen.blit(self.arrowSouth, ((remainder / 2) + i * (self.arrowEast.get_width() + self.spacing), 3))

		elif self.direction == Direction.EAST:
			remainder = self.rect.height % (self.arrowEast.get_height() + self.spacing)
			for i in (0, (self.rect.height // (self.arrowEast.get_height() + self.spacing)) - 1):
				screen.blit(self.arrowEast, (3, (remainder / 2) + i * (self.arrowEast.get_height() + self.spacing)))

		elif self.direction == Direction.WEST:
			remainder = self.rect.height % (self.arrowEast.get_height() + self.spacing)
			for i in (0, (self.rect.height // (self.arrowEast.get_height() + self.spacing)) - 1):
				screen.blit(self.arrowWest, (3, (remainder / 2) + i * (self.arrowEast.get_height() + self.spacing)))

	def transformArrows(self):
		if self.direction == Direction.NORTH:
			self.arrowNorth = pygame.transform.scale(self.arrowNorth, (int(self.rect.width ** 0.75), self.rect.height - 6))

		elif self.direction == Direction.SOUTH:
			self.arrowSouth = pygame.transform.scale(self.arrowNorth, (int(self.rect.width ** 0.75), self.rect.height - 6))

		elif self.direction == Direction.EAST:
			self.arrowEast = pygame.transform.scale(self.arrowNorth, (self.rect.width - 6, int(self.rect.height ** 0.75)))

		elif self.direction == Direction.WEST:
			self.arrowWest = pygame.transform.scale(self.arrowNorth, (self.rect.width - 6, int(self.rect.height ** 0.75)))
