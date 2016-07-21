import pygame
import os
from main.python.physicssim.physics.particle import Particle

class DraggableParticle:
	def __init__(self, pos, mass, charge, timeInterval):
		self.pos = pos
		self.mass = mass
		self.charge = charge
		self.timeInterval = timeInterval
		thisdir = os.path.dirname(__file__)
		self.dir = os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))

	def draw(self, screen):
		if self.charge < 0:
			pic = pygame.image.load(self.dir + "\\negativeparticle.png")
		else:
			pic = pygame.image.load(self.dir + "\\positiveparticle.png")
		pic = pygame.transform.scale(pic, (40, 40))
		screen.blit(pic, self.pos)

	def getObject(self):
		"""Returns object to add to list for drawing"""
		return Particle(self.pos, self.mass, self.charge, self.timeInterval)