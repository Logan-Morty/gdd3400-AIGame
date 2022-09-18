from Vector import Vector
from Constants import *
from Agent import Agent
import pygame
import random

class Enemy(Agent):
	def __init__(self, position, size, speed, color):
		super().__init__(position, size, speed, color)
		self.isFleeing = False
		self.target = Vector(0, 0)

	def switchMode(self):
		self.isFleeing = not self.isFleeing

	def isPlayerClose(self, player):
		if (player.center - self.center).length() < MIN_ATTACK_DIST:
			self.isFleeing = True
			return True
		self.isFleeing = False
		return False

	def calcTrackingVelocity(self, player):
		"""update target vector to point where the agent is targeting"""
		self.target = player.center

	def flee_and_wander(self, player):
		if self.isPlayerClose(player):
			#set target pointing to player
			self.calcTrackingVelocity(player)
			#set velocity to direction opposite of player
			self.velocity = (self.target - self.center).scale(-1)
		else:
			if self.velocity.length() == 0:
				self.velocity = Vector(random.random(), random.random())
			else:
				#set wanderVec perp to velocity and scale by random length then add to velocity to get new direction
				wanderVec = Vector(-self.velocity.y, self.velocity.x)
				wanderVec = wanderVec.scale((random.random()*WANDER_VECTOR_LENGTH) - (WANDER_VECTOR_LENGTH/2))
				self.velocity += wanderVec

	def isInCollision(self, player):
		#this could be updated to be called by player to prevent additional detections
		if super().isInCollision(player):
			self.color = RED

	def draw(self, screen):
		super().draw(screen)
		#draw line to position targeted, aka opposite of targetted player
		if self.isFleeing:
			pygame.draw.line(screen, (255, 0, 0), self.center.tuple(), self.target.tuple(), 1)

	def update(self, player, worldBounds):
		self.flee_and_wander(player)
		self.isInCollision(player)
		super().update(worldBounds)

