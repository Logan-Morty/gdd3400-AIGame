from Vector import Vector
import pygame

class Agent:
	def __init__(self, position, size, speed, color):
		self.position = position
		self.size = Vector(size, size)
		self.speed = speed
		self.velocity = Vector(0, 0)
		self.updateCenter()
		self.updateRect()
		self.color = color

	def __str__(self):
		return "Size:" + str(self.size.x) + "\nPosition:" + str(self.position) +  "\nVelocity:" + str(self.velocity)

	def updateCenter(self):
		"""calculate the agent's center based on position and size"""
		self.center = Vector(self.position.x + (self.size.x/2)-1, self.position.y + (self.size.x/2)-1)

	def updateRect(self):
		"""update the pygame rect based on position and size"""
		self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

	def updateVelocity(self):
		"""normalize the agent's velocity"""
		self.velocity = self.velocity.normalize()

	def isInCollision(self, agent):
		"""returns True if self and agent are in collision"""
		if self.agentRect.colliderect(agent.agentRect):
			return True
		return False

	def draw(self, screen):
		#draw agentRect
		pygame.draw.rect(screen, self.color, self.agentRect)
		#draw velocity vector from center of agent
		pygame.draw.line(screen, (0, 0, 255), self.center.tuple(), 
				   (self.velocity.scale(self.size.x*2) + self.center).tuple(), 2)

	def update(self, worldBounds):
		self.updateVelocity()
		self.position += self.velocity.scale(self.speed)

		#prevent going outside bounds
		self.position = Vector(min(worldBounds[0] - self.size.x, max(0, self.position.x)), 
							   min(worldBounds[1] - self.size.y, max(0, self.position.y)))

		self.updateRect()
		self.updateCenter()