from Vector import Vector
from Agent import Agent
import pygame

class Player(Agent):
    def draw(self, screen):
        super().draw(screen)

    def keyboard_control(self):
        pressed = pygame.key.get_pressed()
        self.velocity = Vector(0,0)

        if pressed[pygame.K_w]: self.velocity.y -= 1
        if pressed[pygame.K_s]: self.velocity.y += 1
        if pressed[pygame.K_a]: self.velocity.x -= 1
        if pressed[pygame.K_d]: self.velocity.x += 1

    def seek(self, enemies):
        closest = 0
        if len(enemies) > 0:
            for i in range(0, len(enemies)):
                chaseVec = enemies[i].center - self.center
                if chaseVec.length() < (enemies[closest].center - self.center).length():
                    closest = i
            self.velocity = enemies[closest].center - self.center


    def detectCollisions(self, enemies):
        for enemy in enemies:
            if self.agentRect.colliderect(enemy.agentRect) and enemy.tagged == 0:
                self.tagged += 1
                enemies.remove(enemy)

    def update(self, enemies, worldBounds):
        self.keyboard_control()
        self.seek(enemies)
        super().update(worldBounds)
        self.detectCollisions(enemies)