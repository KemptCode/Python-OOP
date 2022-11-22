import os
import time
from typing import Tuple
import pygame
from collections import defaultdict

from terrain import Terrain
from lander import Lander
from Point2D import Point2D

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

TIME_BETWEEN_FRAMES = 0.04

GRAVITY_CONST = -0.01
OUTER_BORDER_WIDTH = 30

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
        self.terrain = Terrain(CANVAS_WIDTH, CANVAS_HEIGHT)

        # Lander
        self.lander = Lander(Point2D(CANVAS_WIDTH//2,0)) # add starting position

    def run(self) -> None:
        self.game_screen = RenderEngine()

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
            # TODO: Add out of bounds
            if self.lander.has_crashed() or self.lander_out_of_bounds():
                # Display Game Over Screen
                # TODO: ADD GAME OVER text

                self.game_screen.display_game_over()
                pygame.display.flip()

                time.sleep(TIME_BETWEEN_FRAMES * 100)
                continue

            # Update Physics
            self.lander.apply_gravity(GRAVITY_CONST)
            self.lander.apply_physics()

            # Thrusters
            for key in self.keys_pressed:
                # Lander
                if self.keys_pressed[key] == True:
                    if key == DOWN_BUTTON:
                        self.lander.thrust_down()
                    elif key == LEFT_BUTTON:
                        self.lander.thrust_left()
                    elif key == RIGHT_BUTTON:
                        self.lander.thrust_right()
                    
            # Render Frame
            #   Background
            self.game_screen.display_background()
            self.game_screen.display_fuel(self.lander.fuel)
            #   Stars
            #   Terrain
            self.game_screen.display_lines_between_points(self.terrain.points)
            #   Lander
            self.game_screen.display_lander(self.lander.position)

            pygame.display.flip()
            # Timing
            time.sleep(TIME_BETWEEN_FRAMES)

    def lander_out_of_bounds(self):
        x, y = self.lander.position.x, self.lander.position.y
        return not ((0 - OUTER_BORDER_WIDTH) < x < (CANVAS_WIDTH + OUTER_BORDER_WIDTH) and (0 - OUTER_BORDER_WIDTH) < y < (CANVAS_HEIGHT + OUTER_BORDER_WIDTH))

class RenderEngine:
    def __init__(self) -> None:
        pygame.init()
        # Game window setup
        self.__display = pygame.display.set_mode([CANVAS_WIDTH, CANVAS_HEIGHT])

        # Load images
        self.__lander_img = pygame.image.load(os.path.join("Assets", "Lander.png")).convert()
    
    def display_background(self, bg_color: Tuple[int] = (0, 0, 0)):
        pygame.draw.rect(self.__display, bg_color, [0,0, CANVAS_WIDTH, CANVAS_HEIGHT])

    def display_lander(self, position : Point2D) -> None:
        self.__display.blit(self.__lander_img, (position.x, position.y))
    
    def display_fuel(self, fuel_level):
        # Font
        font = pygame.font.SysFont("Ariel", 24)
        # text surface
        text_surface = font.render(str(fuel_level), False, (0, 200, 0))
        self.__display.blit(text_surface, (0, 0))
    
    def display_game_over(self):
        # Font
        font = pygame.font.SysFont("Ariel", 35)
        # text surface
        text_surface = font.render("Game Over", False, (0,200,0))
        self.__display.blit(text_surface, (CANVAS_WIDTH//2, CANVAS_HEIGHT//2))

    def display_lines_between_points(self, points: Tuple[Point2D]):
        # Draw lines between pair
        for index in range(len(points) - 1):
            pygame.draw.line(self.__display, (255, 255, 255), points[index].to_tuple(), points[index+1].to_tuple(), width=1)


if __name__ == "__main__":
    game = Game()
    game.run()