import math

from main.python.physicssim.graphics.GraphicalParticle import Charge, GraphicalParticle


class Particle:
	def __init__(self, position, mass, charge, timeInterval):
		"""Takes position as list [x, y], mass, charge (sign indicates positive or negative), and the
		amount of time that passes between value calculations (the time between frames shown)"""
		self.moveState = False
		self.pos = position
		self.mass = mass
		self.velocity = [0, 0]
		self.charge = charge
		self.timeInterval = timeInterval
		#setting radius to 20x the mass of particle, can change later
		if self.charge < 0: 
			self.graphicalObject = GraphicalParticle(self.pos, self.mass*20, Charge.NEGATIVE, (0, 0, 255))
		else: 
			self.graphicalObject = GraphicalParticle(self.pos, self.mass*20, Charge.POSITIVE, (255, 0, 0))
		


	def getPos(self):
		"""returns position of particle as list [x, y]"""
		return [self.pos[0], self.pos[1]]

	def getMass(self):
		"""returns mass of particle"""
		return self.mass

	def getVelocity(self):
		"""return velocity of partice as list [x component, y component]"""
		return [self.velocity[0], self.velocity[1]]

	def getCharge(self):
		"""returns charge of particle"""
		return self.charge

	@staticmethod
	def sinatan(x):
		"""Internally used function, returns sine of the arc tangent of the parameter"""
		return x/math.sqrt((x**2)+1)

	@staticmethod
	def cosatan(x):
		"""Internally used function, returns cosine of the arc tangent of the parameter"""
		return 1 / math.sqrt((x ** 2) + 1)


	@staticmethod
	def distance(pos1, pos2):
		"""Internally used function, takes 2 position tuples (x, y) and returns the distance between them"""
		return ((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5

	@staticmethod
	def arcTanWithChecks(x, y):
		"""Performs the arctangent function on the given fraction (y/x)and handles division by zero"""
		if x == 0 and y > 0:
			return math.pi / 2
		elif x == 0 and y < 0:
			return 3 * math.pi / 4
		elif x == 0 and y == 0:
			return 0
		else:
			return math.atan(y/x)

	@classmethod
	def crossProduct(cls, vec1, vec2):
		"""Internally used function, takes 2 2-D vectors as tuples and returns the magnitude (with sign)
		of the resulting cross product"""
		theta1 = cls.arcTanWithChecks(vec1[0], vec1[1])
		theta2 = cls.arcTanWithChecks(vec2[0], vec2[1])
		mag1 = cls.distance((0, 0), vec1)
		mag2 = cls.distance((0,0),  vec2)
		return math.sin(theta1-theta2)*mag1*mag2

	def calculateNetMagneticFieldForce(self, particleList):
		"""Internally used method, returns force due to magnetic field effects
		as tuple (x component, y component)"""
		netMagField = 0
		for p in particleList:
			if not(p is self):
				displacementVec = (p.getPos()[0] - self.pos[0], p.getPos()[1] - self.pos[1])
				cross = self.crossProduct(p.getVelocity(), displacementVec)
				distance = self.distance((0, 0), displacementVec)
				netMagField += (10**-7) * p.getCharge() * cross/distance
		magnitudeV = self.distance((0, 0), self.velocity)
		magnitudeF = magnitudeV * netMagField
		#subtract pi/2 from angle of v to get angle of f
		angleV = self.arcTanWithChecks(self.velocity[0], self.velocity[1])
		angleF = angleV - math.pi/2
		return magnitudeF*math.cos(angleF), magnitudeF*math.sin(angleF)

	def calculateNetCoulombsLawForce(self, particleList):
		"""Internally used method, returns force due to electric interaction with other charged particles
		as tuple (x component, y component)"""
		force = [0, 0]
		for p in particleList:
			if not(p is self):
				magnitude = 8.99*(10**9) * self.charge * p.getCharge() / (self.distance(self.pos, p.getPos())**2)
				#special case so that we don't get division by zero
				if self.pos[0] - p.getPos()[0] == 0:
					force[0] += 0
					force[1] += magnitude
				else:
					angleSlope = (self.pos[1]-p.getPos()[1])/(self.pos[0]-p.getPos()[0])
					force[0] += self.cosatan(angleSlope)*magnitude * math.copysign(1.0, self.pos[0]-p.getPos()[0])
					force[1] += self.sinatan(angleSlope)*magnitude * math.copysign(1.0, self.pos[0]-p.getPos()[0])
		return force[0], force[1]


	def isInside(self, staticField):
		"""Internally used method that checks if particle is inside a given electric field"""
		if self.pos[0] > staticField.topLeft[0] and self.pos[0] < staticField.bottomRight[0]:
			if self.pos[1] > staticField.topLeft[1] and self.pos[1] < staticField.bottomRight[1]:
				return True
		return False

	def calculateNetElectricFieldForce(self, staticFieldList):
		"""Internally used method, returns force due to influence of static electric field on particle
		as tuple (x component, y component)"""
		force = [0, 0]
		for ef in staticFieldList:
			if self.isInside(ef):
				magnitude = self.charge * ef.getStrength()
				force[0] += magnitude*math.cos(ef.getDirection())
				force[1] += magnitude*math.sin(ef.getDirection())
		return force[0], force[1]


	def calculateDisplacement(self, particleList, staticFieldList):
		"""takes list of other particles and static fields in the system,
		updates internal dx and dy variables"""
		if self.moveState:
			self.newVelocity = (0, 0)
			self.dx = 0
			self.dy = 0
		else:
			mff = self.calculateNetMagneticFieldForce(particleList)
			clf = self.calculateNetCoulombsLawForce(particleList)
			eff = self.calculateNetElectricFieldForce(staticFieldList)
			acceleration = ((mff[0]+clf[0]+eff[0])/self.mass, (mff[1]+clf[1]+eff[1])/self.mass)
			#change in velocity is acceleration*time
			self.newVelocity = (self.velocity[0] + acceleration[0]*self.timeInterval,
								self.velocity[1] + acceleration[1]*self.timeInterval)
			self.dx = self.velocity[0]*self.timeInterval + 0.5*acceleration[0]*self.timeInterval
			self.dy = self.velocity[1]*self.timeInterval + 0.5*acceleration[1]*self.timeInterval


	def finalizeValues(self):
		"""Indicates to particle object that all other particle object calculations are done,
		so that internal values can be updated and used for rendering"""
		self.pos = [self.pos[0] + self.dx, self.pos[1] + self.dy]
		self.velocity = self.newVelocity
		self.graphicalObject.update(self.pos, self.mass*20, Charge.NEGATIVE if self.charge < 0 else Charge.POSITIVE)

	def draw(self, screen):
		"""Draws objects using GraphicalParticle"""
		self.graphicalObject.draw(screen)


