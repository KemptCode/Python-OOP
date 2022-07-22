from Point2D import Point2D

# Generate Terrain
class Terrain():
    '''
    Generates a number of points
    Sets a platform for landing
    '''
    def __init__(self, num_points = 20) -> None:
        self.__generate_terrain(num_points)

    def __generate_terrain(self, num_points):
        self.points = [0] * num_points
        self.platform_pos = Point2D()
    
    def get_platform_position(self):
        return self.platform_pos

    def get_terrain_height_at(x):
        pass

