import pygame
import os
from main.python.physicssim.physics.particle import Particle
from main.python.physicssim.graphics.GraphicalParticle import Charge
from main.python.physicssim.menuItems.Size import Size
from main.python.physicssim.menuItems.Strength import Strength

class DraggableParticle:
	def __init__(self, pos, charge):
		"""Pass pos as list [x, y], pass charge as Charge enum"""
		self.moveState = False
		self.pos = pos
		self.charge = charge
		thisdir = os.path.dirname(__file__)
		self.dir = os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))

	def draw(self, screen):
<<<<<<< HEAD
		if self.charge == 2:
=======
		if self.charge == Charge.NEGATIVE:
>>>>>>> 1818ab1da8246a02b478ae51e80f67e0b6b339b3
			pic = pygame.image.load(self.dir + "\\negativeparticle.png")
		else:
			pic = pygame.image.load(self.dir + "\\positiveparticle.png")
		pic = pygame.transform.scale(pic, (40, 40))
		pic.set_colorkey((255, 255, 255))
		screen.blit(pic, self.pos)

	def mouseCollision(self, event):
		if self.pos[0] < event.pos[0] < self.pos[0] + 40:
			if self.pos[1] < event.pos[1] < self.pos[1] + 40:
				return True
		return False

	def getObject(self, size, strength, timeInterval):
		"""Returns object to add to list for drawing;
		size as Size enum, strength as Strength enum, timeInterval is time between updates"""
		if size == Size.SMALL:
			mass = 1
		elif size == Size.MED:
			mass = 2
		else:
			mass = 3

		if strength == Strength.LOW:
			charge = .01
		elif strength == Strength.MED:
			charge = .02
		else:
			charge = .03

		if self.charge == Charge.NEGATIVE:
			charge *= -1

		return Particle(self.pos, mass, self.charge, timeInterval)