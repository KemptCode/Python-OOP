import pygame
pygame.init()

import time
import _thread

from terrain import Terrain
from lander import Lander

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# Game window setup
screen = pygame.display.set_mode([CANVAS_WIDTH, CANVAS_HEIGHT])

# Game elements setup
    # BackGround
    # Terrain
    # Lander


#Game loop
running = True
while running:

    # Handle Events
    for event in pygame.event.get():

        # EXIT
        if event.type == pygame.QUIT:
            running = False
    
    # Calc time delta since last frame

    # Render Frame
        # Background
        # Terrain
        # Lander

    # Update Physics
        # Lander

    # Timing
    time.sleep(.04)