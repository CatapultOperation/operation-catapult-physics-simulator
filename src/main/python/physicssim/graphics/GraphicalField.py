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
		self.spacing = strength // 50
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.rect = pygame.Rect(topLeft, (bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]))
		self.direction = direction
		self.color = color
		self.visualRect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
		self.initArrows()

	def update(self, topLeft, bottomRight, direction, strength, color=(0, 0, 255)):
		self.spacing = strength // 50
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.rect = pygame.Rect(topLeft, (bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]))
		self.direction = direction
		self.color = color
		self.initArrows()

	def draw(self, screen):
		rectSurface = pygame.Surface((self.rect.width, self.rect.height))
		rectSurface.fill((255, 255, 255))
		self.drawArrow(rectSurface)
		pygame.draw.rect(rectSurface, self.color, self.visualRect, 1)
		screen.blit(rectSurface, self.topLeft)

	def mouseCollision(self, event):
		return self.rect.collidepoint(event.pos)

	def initArrows(self):
		arrow = pygame.Surface((300, 100))
		arrow.fill((255, 255, 255))
		pygame.draw.line(arrow, (0, 0, 0), (20, 50), (280, 50), 1)
		pygame.draw.line(arrow, (0, 0, 0), (280, 50), (220, 20), 1)
		pygame.draw.line(arrow, (0, 0, 0), (280, 50), (220, 80), 1)
		self.arrowNorth = pygame.transform.rotate(arrow, 90)
		self.arrowSouth = pygame.transform.rotate(arrow, -90)
		self.arrowEast = arrow
		self.arrowWest = pygame.transform.rotate(arrow, 180)
	
	def drawArrow(self, screen):
		self.transformArrows()
		
		
		
		if self.direction == Direction.NORTH:
			horizontalTotalHeight = self.arrowNorth.get_width() + self.spacing
			horizontalRemainder = self.rect.width % horizontalTotalHeight
			horizontalArrows = self.rect.width // horizontalTotalHeight
			
			for i in range(horizontalArrows):
				screen.blit(self.arrowNorth, ((horizontalRemainder // 2 + self.spacing // 2) + i * horizontalTotalHeight), 3)

		elif self.direction == Direction.SOUTH:
			horizontalTotalHeight = self.arrowSouth.get_width() + self.spacing
			horizontalRemainder = self.rect.width % horizontalTotalHeight
			horizontalArrows = self.rect.width // horizontalTotalHeight
			
			for i in range(horizontalArrows):
				screen.blit(self.arrowSouth, ((horizontalRemainder // 2 + self.spacing // 2) + i * horizontalTotalHeight), 3)
			
		elif self.direction == Direction.EAST:
			verticalTotalHeight = self.arrowEast.get_height() + self.spacing
			verticalRemainder = self.rect.height % verticalTotalHeight
			verticalArrows = self.rect.height // verticalTotalHeight
			
			for i in range(verticalArrows):
				screen.blit(self.arrowEast, (3, (verticalRemainder // 2 + self.spacing // 2) + i * verticalTotalHeight))
			
		elif self.direction == Direction.WEST:
			verticalTotalHeight = self.arrowWest.get_height() + self.spacing
			verticalRemainder = self.rect.height % verticalTotalHeight
			verticalArrows = self.rect.height // verticalTotalHeight
			
			for i in range(verticalArrows):
				screen.blit(self.arrowWest, (3, (verticalRemainder // 2 + self.spacing // 2) + i * verticalTotalHeight))

	def transformArrows(self):
		if self.direction == Direction.NORTH:
			self.arrowNorth = pygame.transform.scale(self.arrowNorth, (int(self.rect.width ** 0.75), self.rect.height - 6))

		elif self.direction == Direction.SOUTH:
			self.arrowSouth = pygame.transform.scale(self.arrowSouth, (int(self.rect.width ** 0.75), self.rect.height - 6))

		elif self.direction == Direction.EAST:
			self.arrowEast = pygame.transform.scale(self.arrowEast, (self.rect.width - 6, int(self.rect.height ** 0.75)))

		elif self.direction == Direction.WEST:
			self.arrowWest = pygame.transform.scale(self.arrowWest, (self.rect.width - 6, int(self.rect.height ** 0.75)))
