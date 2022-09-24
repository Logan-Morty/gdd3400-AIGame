import pygame
from Vector import Vector

FRAME_RATE = 60

#debugging constants:
ENABLE_DOG = True
ENABLE_ALIGNMENT = True
ENABLE_COHESION = True
ENABLE_SEPARATION = True
ENABLE_BOUNDARIES = True

DEBUGGING = False or True
DEBUG_LINE_WIDTH = 1
DEBUG_VELOCITY = DEBUGGING
DEBUG_BOUNDARIES = DEBUGGING
DEBUG_NEIGHBORS = DEBUGGING
DEBUG_DOG_INFLUENCE = DEBUGGING
DEBUG_BOUNDING_RECTS = DEBUGGING

#world constants
WORLD_WIDTH = 1024
WORLD_HEIGHT = 768
WORLD_SIZE = (WORLD_WIDTH, WORLD_HEIGHT)
BOUNDARY_NORMAL_VECTORS = [Vector(1,0), Vector(-1,0), Vector(0,1), Vector(0,-1)]#normal to: [left, right, top, bottom]

#colors
BACKGROUND_COLOR = (100, 149, 237)
YELLOW = (255,255,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

#agent constants:
BOUNDARY_THRESHOLD = 40
AGENT_WIDTH = 16
AGENT_HEIGHT = 32

#dog constants:
DOG_SIZE = 10
DOG_SPEED = 5.5
SEEK_WEIGHT = 0.5
DOG_TURNING_SPEED = 0.4

#sheep constants:
SHEEP_SIZE = 10
SHEEP_SPEED = 5
WANDER_VECTOR_LENGTH = 1.5
MIN_ATTACK_DIST = 200
WANDER_WEIGHT = 0.5
SHEEP_TURNING_SPEED = 0.13
#flocking force constants:
BOUNDARY_WEIGHT = 0.05
FLEE_WEIGHT = 0.5
ALIGNMENT_WEIGHT = 0.5
SEPARATION_WEIGHT = 0.5
COHESION_WEIGHT = 0.5

