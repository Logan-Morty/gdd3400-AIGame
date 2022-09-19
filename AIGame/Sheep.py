from Vector import Vector
from Constants import *
from Agent import Agent
import pygame
import random

class Sheep(Agent):
	def __init__(self, position, image, speed, color, turning_speed):
		super().__init__(position, image, speed, color, turning_speed)
		self.isFleeing = False
		self.targetAgentVector = Vector(0, 0)

	def switchMode(self):
		self.isFleeing = not self.isFleeing

	def isPlayerClose(self, player):
		if (player.center - self.center).length() < MIN_ATTACK_DIST:
			self.isFleeing = True
			return True
		self.isFleeing = False
		return False

	def calcTrackingVelocity(self, player):
		"""update targetAgentVector to point where the agent is targeting"""
		self.targetAgentVector = player.center

	def updateForces(self):
		if self.isFleeing:
			self.fleeWanderForce = self.fleeWanderForce.normalize().scale(FLEE_WEIGHT)
		else:
			self.fleeWanderForce = self.fleeWanderForce.normalize().scale(WANDER_WEIGHT)
		self.target = self.fleeWanderForce

	def flee_and_wander(self, player):
		if self.isPlayerClose(player):
			#set targetAgentVector pointing to player
			self.calcTrackingVelocity(player)
			#set velocity to direction opposite of player
			self.fleeWanderForce = (self.targetAgentVector - self.center).scale(-1)
		else:
			if self.velocity.length() == 0:
				self.fleeWanderForce = Vector(random.random(), random.random())
			else:
				#set wanderVec perp to velocity and scale by random length then add to velocity to get new direction
				wanderVec = Vector(-self.velocity.y, self.velocity.x)
				wanderVec = wanderVec.scale((random.random()*WANDER_VECTOR_LENGTH) - (WANDER_VECTOR_LENGTH/2))
				self.fleeWanderForce = self.velocity + wanderVec
		self.updateForces()

	def isInCollision(self, player):
		#this could be updated to be called by player to prevent additional detections
		if super().isInCollision(player):
			self.color = RED

	def draw(self, screen):
		super().draw(screen)
		#draw line to position targetAgentVector, aka opposite of targetAgent
		if self.isFleeing:
			pygame.draw.line(screen, RED, self.center.tuple(), self.targetAgentVector.tuple(), 1)

	def update(self, player, worldBounds):
		self.flee_and_wander(player)
		self.isInCollision(player)
		super().update(worldBounds)

