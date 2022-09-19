import pygame
from Constants import *
from Dog import Dog
from Sheep import Sheep
from Vector import Vector
import random

pygame.init()
screen = pygame.display.set_mode(WORLD_SIZE)
pygame.display.set_caption("Rectangle Tag!")

sheepImage = pygame.image.load("sheep.png")
dogImage = pygame.image.load("dog.png")

quit = False
clock = pygame.time.Clock()

dog = Dog(Vector(WORLD_WIDTH/2, WORLD_HEIGHT/2), dogImage, DOG_SPEED, YELLOW, DOG_TURNING_SPEED)
sheepList = []
for i in range(10):
	sheepList.append(Sheep(Vector(random.randint(0,WORLD_WIDTH), random.randint(0, WORLD_HEIGHT)), sheepImage, SHEEP_SPEED, GREEN, SHEEP_TURNING_SPEED))
drawnSheep = sheepList.copy()


while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
	clock.tick(FRAME_RATE)
	screen.fill(BACKGROUND_COLOR)

	#call agent draw and update methods here:
	dog.update(sheepList, WORLD_SIZE)

	title = "Rectangle Tag! remaining: " + str(len(sheepList))
	pygame.display.set_caption(title)


	dog.draw(screen)
	for sheep in drawnSheep:
		sheep.update(dog, WORLD_SIZE)
		sheep.draw(screen)

	pygame.display.flip()