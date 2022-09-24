from Vector import Vector
from Agent import Agent
import Constants
import pygame

class Dog(Agent):
	def __init__(self, position, image, speed, color, turning_speed):
		super().__init__(position, image, speed, color, turning_speed)
		self.targetAgent = None

	def keyboard_control(self):
		pressed = pygame.key.get_pressed()
		#self.velocity = Vector(0,0)

		if pressed[pygame.K_w]: self.velocity.y -= 1
		if pressed[pygame.K_s]: self.velocity.y += 1
		if pressed[pygame.K_a]: self.velocity.x -= 1
		if pressed[pygame.K_d]: self.velocity.x += 1

	def updateForces(self):
		self.seekForce = (self.targetAgent.center - self.center).normalize().scale(Constants.SEEK_WEIGHT)
		self.target = self.seekForce

	def seek(self, agents):
		if len(agents) > 0:
			self.targetAgent = agents[0]
			for agent in agents:
				if (agent.center - self.center).length() < (self.targetAgent.center - self.center).length():
					self.targetAgent = agent
			self.updateForces()

	def isInCollision(self, agents):
		for agent in agents:
			if super().isInCollision(agent):
				agents.remove(agent)

	def update(self, sheep, worldBounds):
		self.keyboard_control()
		self.seek(sheep)
		self.isInCollision(sheep)
		super().update(worldBounds)
