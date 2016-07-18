class Particle:
	def __init__(self, position, mass, charge):
		"""Takes position as tuple (x, y), mass, and change (sign indicates positive or negative)"""
		self.pos = position
		self.mass = mass
		self.velocity = (0, 0)
		self.charge = charge

	def getPosition(self):
		"""returns position of particle as tuple (x, y)"""
		return self.pos

	def getMass(self):
		"""returns mass of particle"""
		return self.mass

	def getVelocity(self):
		"""return velocity of partice as tuple (x component, y component)"""
		return self.velocity

	def getCharge(self):
		"""returns charge of particle"""
		return self.charge

	def calculateDisplacement(self, particleList, staticFieldList):
		"""takes list of other particles and static fields in the system
		returns the change in position as tuple (x, y) for period of time elapsed by main loop"""