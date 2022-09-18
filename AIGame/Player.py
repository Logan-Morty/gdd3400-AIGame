from Vector import Vector
from Agent import Agent
import pygame

class Player(Agent):
	def __init__(self, position, size, speed, color):
		super().__init__(position, size, speed, color)
		self.targetAgent = None

	def keyboard_control(self):
		pressed = pygame.key.get_pressed()
		self.velocity = Vector(0,0)

		if pressed[pygame.K_w]: self.velocity.y -= 1
		if pressed[pygame.K_s]: self.velocity.y += 1
		if pressed[pygame.K_a]: self.velocity.x -= 1
		if pressed[pygame.K_d]: self.velocity.x += 1

	def seek(self, enemies):
		if len(enemies) > 0:
			self.targetAgent = enemies[0]
			for enemy in enemies:
				if (enemy.center - self.center).length() < (self.targetAgent.center - self.center).length():
					self.targetAgent = enemy
			self.velocity = self.targetAgent.center - self.center

	def isInCollision(self, enemies):
		for enemy in enemies:
			if super().isInCollision(enemy):
				enemies.remove(enemy)

	def update(self, enemies, worldBounds):
		self.keyboard_control()
		self.seek(enemies)
		self.isInCollision(enemies)
		super().update(worldBounds)
