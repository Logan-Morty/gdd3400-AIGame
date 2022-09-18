from Vector import Vector
import pygame

class Agent:
    def __init__(self, position, size, speed, color):
        self.position = position
        self.size = size
        self.speed = speed
        self.velocity = Vector(0, 0)
        self.center = self.calcCenter()
        self.color = color
        self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.tagged = 0

    def __str__(self):
        return "Size:" + str(self.size) + "\nPosition:" + str(self.position) +  "\nVelocity:" + str(self.velocity)

    def calcCenter(self):
        return Vector(self.position.x + (self.size/2)-1, self.position.y + (self.size/2)-1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.agentRect)
        displayVelocity = self.velocity.scale(self.size*2) + self.center
        pygame.draw.line(screen, (0, 0, 255), (self.center.x, self.center.y), (displayVelocity.x, displayVelocity.y), 2)

    def update(self, worldBounds):
        self.agentRect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        self.velocity = self.velocity.normalize().scale(self.speed)
        
        self.position += self.velocity
        oldPos = self.position

        self.position = Vector(min(worldBounds[0] - self.size, max(0, self.position.x)), 
                               min(worldBounds[1] - self.size, max(0, self.position.y)))
        self.center = self.calcCenter()