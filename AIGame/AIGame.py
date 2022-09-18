import pygame
from Constants import *
from Player import Player
from Enemy import Enemy
from Vector import Vector
import random

pygame.init()
screen = pygame.display.set_mode(WORLD_SIZE)
pygame.display.set_caption("Rectangle Tag!")

quit = False
clock = pygame.time.Clock()

player = Player(Vector(WORLD_WIDTH/2, WORLD_HEIGHT/2), PLAYER_SIZE, PLAYER_SPEED, YELLOW)
#enemy = Enemy(Vector(100, 100), ENEMY_SIZE, ENEMY_SPEED, GREEN)
#enemy2 = Enemy(Vector(500, 500), ENEMY_SIZE, ENEMY_SPEED, GREEN)
enemies = []
for i in range(10):
    enemies.append(Enemy(Vector(random.randint(0,WORLD_WIDTH), random.randint(0, WORLD_HEIGHT)), ENEMY_SIZE, ENEMY_SPEED, GREEN))
drawnEnemies = enemies.copy()


while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    clock.tick(FRAME_RATE)
    screen.fill((100, 149, 237))

    #call agent draw and update methods here:
    player.update(enemies, WORLD_SIZE)

    title = "Rectangle Tag! remaining: " + str(len(enemies))
    pygame.display.set_caption(title)


    player.draw(screen)
    for enemy in drawnEnemies:
        enemy.update(player, WORLD_SIZE)
        enemy.draw(screen)

    pygame.display.flip()