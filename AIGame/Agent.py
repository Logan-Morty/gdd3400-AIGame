from Vector import Vector
import Constants
import pygame
import math

class Agent:
	def __init__(self, position, image, speed, color, turning_speed):
		self.position = position
		self.angle = 0
		self.size = Vector(Constants.AGENT_WIDTH, Constants.AGENT_HEIGHT)
		self.image = image
		self.speed = speed
		self.velocity = Vector(0, 0)
		self.updateCenter()
		self.surf = pygame.transform.rotate(self.image, self.angle)
		self.upperLeft = Vector(self.center.x - self.surf.get_width()/2, self.center.y - self.surf.get_height()/2)
		self.updateRect()
		self.color = color
		self.target = Vector(0, 0)
		self.turning_speed = turning_speed

	def __str__(self):
		return "Size:" + str(self.size.x) + "\nPosition:" + str(self.position) +  "\nVelocity:" + str(self.velocity)

	def updateCenter(self):
		"""calculate the agent's center based on position and size"""
		self.center = Vector(self.position.x + (self.size.x/2), self.position.y + (self.size.y/2))

	def updateAngle(self):
		self.angle = math.degrees(math.atan2(self.velocity.x, self.velocity.y))+180

	def updateRect(self):
		"""update the pygame rect based on position and size"""
		self.upperLeft = Vector(self.center.x - self.surf.get_width()/2, self.center.y - self.surf.get_height()/2)
		self.agentRect = self.surf.get_bounding_rect().move(self.upperLeft.x, self.upperLeft.y)
		self.surf = pygame.transform.rotate(self.image, self.angle)

	def updateVelocity(self):
		self.target = self.target.normalize()
		targetDifference = self.target - self.velocity
		if targetDifference.length() < self.turning_speed:
			self.velocity = self.target
		else:
			targetDifference = targetDifference.normalize().scale(self.turning_speed)
			self.velocity += targetDifference
		self.velocity = self.velocity.normalize()

	def isInCollision(self, agent):
		"""returns True if self and agent are in collision"""
		if self.agentRect.colliderect(agent.agentRect):
			return True
		return False

	def calcBoundaryForce(self):
		self.boundForce = Vector(0, 0)
		boundDist = [self.center.x, Constants.WORLD_WIDTH - self.center.x, self.center.y, Constants.WORLD_HEIGHT - self.center.y]
		for i in range(len(boundDist)):
			if boundDist[i] < Constants.BOUNDARY_THRESHOLD:
				self.boundForce += Constants.BOUNDARY_NORMAL_VECTORS[i].scale(Constants.BOUNDARY_THRESHOLD - boundDist[i])
		self.boundForce = self.boundForce.scale(Constants.BOUNDARY_WEIGHT * int(Constants.ENABLE_BOUNDARIES))
		self.target += self.boundForce

	def draw(self, screen):
		#draw agentRect
		if Constants.DEBUG_BOUNDING_RECTS:
			pygame.draw.rect(screen, self.color, self.agentRect, width=2)
		#draw agent's image
		screen.blit(self.surf, self.upperLeft.tuple())
		#draw velocity vector from center of agent
		if Constants.DEBUG_VELOCITY:
			pygame.draw.line(screen, Constants.BLUE, self.center.tuple(), (self.velocity.scale(self.size.x*2) + self.center).tuple(), 2)
		#draw boundary force from center of agent
		if self.boundForce.tuple() != (0, 0) and Constants.DEBUG_BOUNDARIES:
			pygame.draw.line(screen, Constants.ORANGE, self.center.tuple(), (self.center + self.boundForce.normalize().scale(-100)).tuple(), 2)

	def update(self, worldBounds):
		self.calcBoundaryForce()
		self.updateVelocity()
		self.updateAngle()

		self.position += self.velocity.scale(self.speed)

		#prevent going outside bounds
		self.position = Vector(min(worldBounds[0] - self.size.x, max(0, self.position.x)), 
							   min(worldBounds[1] - self.size.y, max(0, self.position.y)))

		self.updateCenter()
		self.updateRect()
