import math

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def tuple(self):
		"""return a tuple storing the vector's x and y"""
		return (self.x, self.y)

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def length(self):
		return math.sqrt((self.x * self.x) + (self.y * self.y))

	def normalize(self):
		"""return vector as a unit vector"""
		if self.length()==0:
			return self
		return Vector(self.x/self.length(), self.y/self.length())

	def scale(self, scalar):
		"""return vector scaled by scalar"""
		return Vector(self.normalize().x * scalar, self.normalize().y * scalar)

	def dot(self, other):
		"""return dot product of vector and other"""
		return self.x*other.x + self.y*other.y
