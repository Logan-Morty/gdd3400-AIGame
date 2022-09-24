from ctypes import alignment
from typing import Concatenate
from Vector import Vector
import Constants
from Agent import Agent
import pygame
import random

class Sheep(Agent):
	def __init__(self, position, image, speed, color, turning_speed):
		super().__init__(position, image, speed, color, turning_speed)
		self.isFleeing = False
		self.targetAgentVector = Vector(0, 0)

	def isPlayerClose(self, player):
		if (player.center - self.center).length() < Constants.MIN_ATTACK_DIST:
			self.isFleeing = True
			return True
		self.isFleeing = False
		return False

	def calcTrackingVelocity(self, player):
		"""update targetAgentVector to point where the agent is targeting"""
		self.targetAgentVector = player.center

	def updateForces(self, fleeForce, alignmentForce, cohesionForce, separationForce):
		if self.isFleeing:
			fleeForce = fleeForce.normalize().scale(Constants.FLEE_WEIGHT * int(Constants.ENABLE_DOG))
		else:
			fleeForce = Vector(0,0)
		alignmentForce = alignmentForce.normalize().scale(Constants.ALIGNMENT_WEIGHT * int(Constants.ENABLE_ALIGNMENT))
		cohesionForce = cohesionForce.normalize().scale(Constants.COHESION_WEIGHT * int(Constants.ENABLE_COHESION))
		separationForce = separationForce.normalize().scale(Constants.SEPARATION_WEIGHT * int(Constants.ENABLE_SEPARATION))
		self.target = fleeForce + alignmentForce + cohesionForce + separationForce

	def flee(self, player):
		if self.isPlayerClose(player):# or True:
			#set targetAgentVector pointing to player
			self.calcTrackingVelocity(player)
			#set force to direction opposite of player
			fleeForce = (player.center - self.center).scale(-1)
			return fleeForce

	def computeAlignment(self, neighborhood):
		alignment = Vector(0,0)
		neighborCount = len(neighborhood)
		for agent in neighborhood:
			alignment += agent.velocity
		if neighborCount == 0:
			return alignment
		alignment.x /= neighborCount
		alignment.y /= neighborCount
		alignment = alignment.normalize()
		return alignment

	def computeCohesion(self, neighborhood):
		cohesion = Vector(0,0)
		neighborCount = len(neighborhood)
		for agent in neighborhood:
			cohesion += agent.center
		if neighborCount == 0:
			return cohesion
		cohesion.x /= neighborCount
		cohesion.y /= neighborCount
		cohesion -= self.center
		cohesion = cohesion.normalize()
		return cohesion

	def computeSeparation(self, neighborhood):
		separation = Vector(0,0)
		neighborCount = 0
		for agent in neighborhood:
			separation += self.center - agent.center
		if neighborCount == 0:
			return separation
		separation.x /= neighborCount
		separation.y /= neighborCount
		separation = separation.normalize()
		return separation

	def isInCollision(self, player):
		#this could be updated to be called by player to prevent additional detections
		if super().isInCollision(player):
			self.color = Constants.RED

	def draw(self, screen, neighborhood):
		super().draw(screen)
		#draw line to position targetAgentVector, aka opposite of targetAgent
		if self.isFleeing and Constants.DEBUG_DOG_INFLUENCE:
			pygame.draw.line(screen, Constants.RED, self.center.tuple(), self.targetAgentVector.tuple(), 1)
		#draw line to each of the sheep's neighbors
		if Constants.DEBUG_NEIGHBORS:
			for neighbor in neighborhood:
				pygame.draw.line(screen, Constants.GREEN, self.center.tuple(), neighbor.center.tuple(), 1)

	def update(self, player, worldBounds, neighborhood):
		self.updateForces(self.flee(player), self.computeAlignment(neighborhood), self.computeCohesion(neighborhood), self.computeSeparation(neighborhood))
		self.isInCollision(player)
		super().update(worldBounds)

