class StaticField:
	def __init__(self, topLeft, bottomRight, strength, direction):
		"""Takes arguments topLeft as tuple (x, y), bottomRight as tuple (x, y), strength (in N/C),
		and direction in radians"""
		self.topLeft = topLeft
		self.bottomRight = bottomRight
		self.strength = strength
		self.direction = direction

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