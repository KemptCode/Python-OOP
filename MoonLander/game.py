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
        self.lander = Lander(Point2D(CANVAS_WIDTH//2, 0)
                             )  # add starting position

    def run(self) -> None:
        self.game_screen = RenderEngine()

        # Game loop
        paused = False

        while True:
            # Handle Events
            
            for event in pygame.event.get():
                # EXIT
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    self.keys_pressed[event.key] = True
                    # print(self.keys_pressed)

                elif event.type == pygame.KEYUP:
                    del self.keys_pressed[event.key]
                    # print(self.keys_pressed)

            # Calc time delta since last frame

            # LOSE Condition
            if self.lander.has_crashed() or self.lander_out_of_bounds():
                # Display Game Over Screen
                
                self.game_screen.display_game_over()
                pygame.display.flip()

                # Wait for user input
                while True:
                    for event in pygame.event.get():
                        # EXIT
                        if event.type == pygame.QUIT:
                            return
                    time.sleep(TIME_BETWEEN_FRAMES)

            # WIN Condition
            if 1024 > ((self.lander.position.x - self.terrain.get_platform_position().x)**2 + (self.lander.position.y - self.terrain.get_platform_position().y)**2):
                # Display Game Over Screen
                
                self.game_screen.display_game_win()
                pygame.display.flip()

                # Wait for user input
                while True:
                    for event in pygame.event.get():
                        # EXIT
                        if event.type == pygame.QUIT:
                            return
                    time.sleep(TIME_BETWEEN_FRAMES)

            # Update Physics
            self.lander.apply_gravity(GRAVITY_CONST)
            self.lander.apply_physics()
            if self.lander.position.y > self.terrain.get_terrain_height_at(self.lander.position.x):
                self.lander.crashed = True

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
            #   Terrain
            self.game_screen.display_lines_between_points(self.terrain.points)
            #   Lander
            self.lander.display_lander(self.game_screen.display_lander)
            self.game_screen.display_marker(self.lander.position)
            #   Platform
            self.game_screen.display_platform(self.terrain.get_platform_position())

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
        self.__lander_img = pygame.image.load(
            os.path.join("Assets", "Lander.png")).convert()
        
        self.__platform_img = pygame.image.load(
            os.path.join("Assets", "Platform.png")).convert()
        
        self.__marker = pygame.image.load(
            os.path.join("Assets", "marker.png")).convert()

    def display_background(self, bg_color: Tuple[int] = (0, 0, 0)):
        self.__display.fill(bg_color)
        # Stars

    def display_lander(self, position: Point2D) -> None:
        self.__display.blit(self.__lander_img, (position.x, position.y))
        
    def display_marker(self, position: Point2D) -> None:
        self.__display.blit(self.__marker, (position.x, position.y))

    def display_platform(self, position: Point2D) -> None:
        self.__display.blit(self.__platform_img, (position.x, position.y))

    def display_fuel(self, fuel_level: int):
        # Font
        font = pygame.font.SysFont("Ariel", 24)
        # text surface
        text_surface = font.render(str(fuel_level), False, (0, 200, 0))
        self.__display.blit(text_surface, (0, 0))

    def display_game_over(self):
        # Font
        font = pygame.font.SysFont("Ariel", 35)
        # text surface
        text_surface = font.render("Game Over", False, (0, 200, 0))
        self.__display.blit(text_surface, (CANVAS_WIDTH//2, CANVAS_HEIGHT//2))

    def display_game_win(self):
        # Font
        font = pygame.font.SysFont("Ariel", 35)
        # text surface
        text_surface = font.render("You won!", False, (0, 200, 0))
        self.__display.blit(text_surface, (CANVAS_WIDTH//2, CANVAS_HEIGHT//2))

    def display_lines_between_points(self, points: Tuple[Point2D]):
        # Draw lines between pair
        for index in range(len(points) - 1):
            pygame.draw.line(self.__display, (255, 255, 255),
                             points[index].to_tuple(),
                             points[index+1].to_tuple(), width=1)


if __name__ == "__main__":
    game = Game()
    game.run()
