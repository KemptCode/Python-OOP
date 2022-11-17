import random
from Point2D import Point2D

# Generate Terrain
class Terrain():
    '''
    Generates a number of points
    Sets a platform for landing
    '''
    def __init__(self, width, height, num_points : int = 20) -> None:
        self.__generate_terrain( width, height, num_points)

    def __generate_terrain(self, width, height, num_points : int) -> None:
        self.points = []
        for i in range(num_points):
            self.points.append(Point2D(i * width//num_points, random.randint(height//2, height)))
        self.platform_pos = Point2D()
    
    def get_platform_position(self) -> Point2D:
        return self.platform_pos

    def get_terrain_height_at(x : int) -> int:
        pass

