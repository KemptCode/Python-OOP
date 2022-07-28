import pygame
import time
from collections import defaultdict

from terrain import Terrain
from lander import Lander
from Point2D import Point2D

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

TIME_BETWEEN_FRAMES = 0.04

GRAVITY_CONST = 0.1

UP_BUTTON = pygame.K_UP
DOWN_BUTTON = pygame.K_DOWN
LEFT_BUTTON = pygame.K_LEFT
RIGHT_BUTTON = pygame.K_RIGHT

class Game:
    def __init__(self) -> None:
    # Game elements setup
        # BackGround
        self.keys_pressed = defaultdict(bool)

        # Terrain
        self.terrain = Terrain()

        # Lander
        self.lander = Lander(Point2D) # add starting position

    def run(self) -> None:
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

                if event.type == pygame.KEYDOWN:
                    self.keys_pressed[event.key] = True
                    print(self.keys_pressed)
                    
                elif event.type == pygame.KEYUP:
                    del self.keys_pressed[event.key]
                    print(self.keys_pressed)

            # Calc time delta since last frame

            # WIN / LOSE ? Conditions
            if self.lander.has_crashed():
                # Display Game Over Screen

                time.sleep(TIME_BETWEEN_FRAMES)
                continue

            # Update Physics
            self.lander.apply_gravity()

            # Thrusters
            for key in self.keys_pressed:
                # Lander
                if self.keys_pressed[key] == True:
                    if key == DOWN_BUTTON:
                        pass
                    elif key == LEFT_BUTTON:
                        pass
                    elif key == RIGHT_BUTTON:
                        pass
                    
            # Render Frame
                # Background
                    #Stars
                # Terrain
                # Lander

            # Timing
            time.sleep(TIME_BETWEEN_FRAMES)

if __name__ == "__main__":
    game = Game()
    game.run()