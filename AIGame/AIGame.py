import pygame
import Constants
from Dog import Dog
from Sheep import Sheep
from Vector import Vector
import random

pygame.init()
screen = pygame.display.set_mode(Constants.WORLD_SIZE)
pygame.display.set_caption("Rectangle Tag!")

sheepImage = pygame.image.load("sheep.png")
dogImage = pygame.image.load("dog.png")

quit = False
clock = pygame.time.Clock()

dog = Dog(Vector(Constants.WORLD_WIDTH/2, Constants.WORLD_HEIGHT/2), dogImage, Constants.DOG_SPEED, Constants.YELLOW, Constants.DOG_TURNING_SPEED)
sheepList = []
for i in range(Constants.NUM_SHEEP):
	sheepList.append(Sheep(Vector(random.randint(0,Constants.WORLD_WIDTH), random.randint(0, Constants.WORLD_HEIGHT)), sheepImage, Constants.SHEEP_SPEED, Constants.GREEN, Constants.SHEEP_TURNING_SPEED))
drawnSheep = sheepList.copy()

def handleDebugging(events):        
	# Handle the Debugging for Forces
	for event in events:
		if event.type == pygame.KEYUP:

			# Toggle Dog Influence
			if event.key == pygame.K_1:
				Constants.ENABLE_DOG = not Constants.ENABLE_DOG
				print("Toggle Dog Influence", Constants.ENABLE_DOG)

			# Toggle Alignment Influence
			if event.key == pygame.K_2: 
				Constants.ENABLE_ALIGNMENT = not Constants.ENABLE_ALIGNMENT
				print("Toggle Alignment Influence", Constants.ENABLE_ALIGNMENT)

			# Toggle Separation Influence
			if event.key == pygame.K_3: 
				Constants.ENABLE_SEPARATION = not Constants.ENABLE_SEPARATION
				print("Toggle Separation Influence", Constants.ENABLE_SEPARATION)

			# Toggle Cohesion Influence
			if event.key == pygame.K_4: 
				Constants.ENABLE_COHESION = not Constants.ENABLE_COHESION
				print("Toggle Cohesion Influence", Constants.ENABLE_COHESION)

			# Toggle Boundary Influence
			if event.key == pygame.K_5: 
				Constants.ENABLE_BOUNDARIES = not Constants.ENABLE_BOUNDARIES
				print("Toggle Boundary Influence", Constants.ENABLE_BOUNDARIES)

			# Toggle Dog Influence Lines
			if event.key == pygame.K_6: 
				Constants.DEBUG_DOG_INFLUENCE = not Constants.DEBUG_DOG_INFLUENCE
				print("Toggle Dog Influence Lines", Constants.DEBUG_DOG_INFLUENCE)
	
			# Toggle Velocity Lines
			if event.key == pygame.K_7: 
				Constants.DEBUG_VELOCITY = not Constants.DEBUG_VELOCITY
				print("Toggle Velocity Lines", Constants.DEBUG_VELOCITY)

			# Toggle Neighbor Lines
			if event.key == pygame.K_8: 
				Constants.DEBUG_NEIGHBORS = not Constants.DEBUG_NEIGHBORS
				print("Toggle Neighbor Lines", Constants.DEBUG_NEIGHBORS)

			# Toggle Boundary Force Lines
			if event.key == pygame.K_9: 
				Constants.DEBUG_BOUNDARIES = not Constants.DEBUG_BOUNDARIES
				print("Toggle Boundary Force Lines", Constants.DEBUG_BOUNDARIES)

			# Toggle Bounding Box Lines
			if event.key == pygame.K_0: 
				Constants.DEBUG_BOUNDING_RECTS = not Constants.DEBUG_BOUNDING_RECTS
				print("Toggle Bounding Box Lines", Constants.DEBUG_BOUNDING_RECTS)

if Constants.DEBUGGING:
	print("Debugging tools:")
	print("1.Toggle Dog Forces")
	print("2.Toggle Alignment Forces")
	print("3.Toggle Separation Forces")
	print("4.Toggle Cohesion Forces")
	print("5.Toggle Boundary Forces")
	print("6.Toggle Dog Force line")
	print("7.Toggle Sheep and Dog Velocity line")
	print("8.Toggle Neighbor lines")
	print("9.Toggle Boundary Force lines")
	print("0.Toggle Bounding Boxes")
	
while not quit:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			quit = True
	clock.tick(Constants.FRAME_RATE)
	screen.fill(Constants.BACKGROUND_COLOR)

	handleDebugging(events)

	#call agent draw and update methods here:
	dog.update(sheepList, Constants.WORLD_SIZE)

	title = "Rectangle Tag! remaining: " + str(len(sheepList))
	pygame.display.set_caption(title)


	dog.draw(screen)
	i = 0
	for sheep in drawnSheep:
		neighborhood = []
		for neighbor in drawnSheep:
			if neighbor is not sheep:
				if (sheep.center - neighbor.center).length() < Constants.SHEEP_NEIGHBOR_RADIUS:
					neighborhood.append(neighbor)

		sheep.update(dog, Constants.WORLD_SIZE, neighborhood)
		sheep.draw(screen, neighborhood)

	pygame.display.flip()