from enum import Enum

import pygame
from pygame import surface


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class GraphicalField:
    def __init__(self, rect, direction, strength, color=(0, 0, 0)):
        self.spacing = 10
        self.rect = rect
        self.direction = direction
        self.update(strength)
        self.color = color
        self.initArrows()
    
    def update(self, strength):
        self.spacing = strength
        
    def draw(self, screen, position):
        rectSurface = pygame.Surface(self.rect.width(), self.rect.height())
        self.drawArrow(screen)
        pygame.draw.rect(rectSurface, self.color, self.rect, 1)
        screen.blit(rectSurface, position)
        
    def initArrows(self):
        arrowEast = pygame.Surface((30, 10))
        pygame.draw.line(self.arrowEast, (0, 0, 0), (2, 5), (28, 5), 1)
        pygame.draw.line(self.arrowEast, (0, 0, 0), (28, 5), (22, 2), 1)
        pygame.draw.line(self.arrowEast, (0, 0, 0), (28, 5), (22, 8), 1)
        self.arrowNorth = pygame.transform.rotate(arrowEast, -90)
        self.arrowSouth = pygame.transform.rotate(arrowEast, 90)
        self.arrowWest = pygame.transform.rotate(arrowEast, 180)
    
    def drawArrow(self, screen):
        self.transformArrows()
        
        if self.direction == Direction.NORTH: 
            remainder = self.rect.width() % (self.arrowEast.get_width() + self.spacing)
            for i in (0, (self.rect.width() // (self.arrowEast.get_width() + self.spacing)) - 1):
                screen.blit(self.arrowNorth, ((remainder / 2) + i * (self.arrowEast.get_width() + self.spacing), 3))
        
        elif self.direction == Direction.SOUTH: 
            remainder = self.rect.width() % (self.arrowEast.get_width() + self.spacing)
            for i in (0, (self.rect.width() // (self.arrowEast.get_width() + self.spacing)) - 1):
                screen.blit(self.arrowSouth, ((remainder / 2) + i * (self.arrowEast.get_width() + self.spacing), 3))
                
        elif self.direction == Direction.EAST: 
            remainder = self.rect.height() % (self.arrowEast.get_height() + self.spacing)
            for i in (0, (self.rect.height() // (self.arrowEast.get_height() + self.spacing)) - 1):
                screen.blit(self.arrowEast, (3, (remainder / 2) + i * (self.arrowEast.get_height() + self.spacing)))
                
        elif self.direction == Direction.WEST: 
            remainder = self.rect.height() % (self.arrowEast.get_height() + self.spacing)
            for i in (0, (self.rect.height() // (self.arrowEast.get_height() + self.spacing)) - 1):
                screen.blit(self.arrowWest, (3, (remainder / 2) + i * (self.arrowEast.get_height() + self.spacing)))
                
    
    def transformArrows(self):
        if self.direction == Direction.NORTH: 
            self.arrowNorth = pygame.transform.scale(self.arrowNorth, (self.rect.width() ** 0.75, self.rect.height() - 6))
            
        elif self.direction == Direction.SOUTH: 
            self.arrowSouth = pygame.transform.scale(self.arrowNorth, (self.rect.width() ** 0.75, self.rect.height() - 6))
            
        elif self.direction == Direction.EAST: 
            self.arrowEast = pygame.transform.scale(self.arrowNorth, (self.rect.width() - 6, self.rect.height() ** 0.75))
            
        elif self.direction == Direction.WEST: 
            self.arrowWest = pygame.transform.scale(self.arrowNorth, (self.rect.width() - 6, self.rect.height() ** 0.75))