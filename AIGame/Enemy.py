from Vector import Vector
from Constants import *
from Agent import Agent
import pygame
import random

class Enemy(Agent):
    def draw(self, screen):
        super().draw(screen)
        pygame.draw.line(screen, (255, 0, 0), (self.center.x, self.center.y), (self.playerVec.x, self.playerVec.y), 1)

    def flee_and_wander(self, player):
        self.playerVec = player.center
        playerDist = self.playerVec - self.center
        fleeVec = playerDist.scale(-1)
        if playerDist.length() < FLEE_RANGE:
            self.velocity = fleeVec
        else:
            if self.velocity.length() == 0:
                self.velocity = Vector(random.random(), random.random())
            else:
                wanderVec = Vector(-self.velocity.y, self.velocity.x)
                wanderVec = wanderVec.scale((random.random()*WANDER_VECTOR_LENGTH) - (WANDER_VECTOR_LENGTH/2))
                self.velocity += wanderVec

    def detectCollisions(self, player):
        if self.agentRect.colliderect(player.agentRect):
            self.tagged = 1
            self.color = RED

    def update(self, player, worldBounds):
        oldPos = self.position
        self.flee_and_wander(player)
        super().update(worldBounds)

        self.detectCollisions(player)

