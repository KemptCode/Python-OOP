import random
from Point2D import Point2D

# Generate Terrain


class Terrain():
    '''
    Generates a number of points
    Sets a platform for landing
    '''

    def __init__(self, width: int, height: int, num_segments: int = 20) -> None:
        self.width = width
        self.height = height
        self.num_segments = num_segments - 1
        self.__generate_terrain(width, height, num_segments)

    def __generate_terrain(self, width: int, height: int, num_segments: int) -> None:
        self.points = []
        for i in range(num_segments + 1):
            self.points.append(Point2D(i * width//num_segments,
                               random.randint(height//2, height)))
        platform_x = random.randint(0, num_segments * (width//num_segments) - 66)
        self.platform_pos = Point2D(platform_x, self.highest_point_in_range(platform_x, platform_x + 64) - 20)

    def get_platform_position(self) -> Point2D:
        return self.platform_pos
    
    def highest_point_in_range(self, x1, x2):
        array = [self.get_terrain_height_at(x1), self.get_terrain_height_at(x2)]

        terrain_width = (self.width // self.num_segments)
        current_index = int(x1 // terrain_width)

        while 0 <= current_index < self.num_segments and current_index * terrain_width <= x2:
            if x1 <= current_index * terrain_width:
                array.append(self.points[current_index].y)
            current_index += 1

        return min(array)

    def get_terrain_height_at(self, x: int) -> int:
        if x < 0 or self.width < x:
            return self.height

        i = int(x // (self.width / self.num_segments))
        p1, p2 = self.points[i], self.points[i+1]


        percent_between_points = (x - p1.x) / (p2.x - p1.x)
        dy = p2.y - p1.y

        return p1.y + dy * percent_between_points