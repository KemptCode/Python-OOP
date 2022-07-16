import pygame
import time

from terrain import Terrain
from lander import Lander
from Point2D import Point2D

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

class Game:
    def __init__(self) -> None:
    # Game elements setup
        # BackGround

        # Terrain
        self.terrain = Terrain()

        # Lander
        self.lander = Lander(Point2D) # add starting position

    def run(self):
        pygame.init()
        # Game window setup
        screen = pygame.display.set_mode([CANVAS_WIDTH, CANVAS_HEIGHT])

        #Game loop
        running = True
        while running:

            # Handle Events
            for event in pygame.event.get():

                # EXIT
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.K_UP:
                    pass

                if event.type == pygame.K_DOWN:
                    pass

                if event.type == pygame.K_LEFT:
                    pass

                if event.type == pygame.K_RIGHT:
                    pass
            
            # Calc time delta since last frame

            # Render Frame
                # Background
                # Terrain
                # Lander

            # Update Physics
                # Lander

            # Timing
            time.sleep(.04)

if __name__ == "__main__":
    game = Game()
    game.run()