from Velocity2D import Velocity2D

class Point2D:
    '''

    '''
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def add_update(self, otherPoint):
        if type(otherPoint) == Point2D:
            self.x += otherPoint.x
            self.y += otherPoint.y
        elif type(otherPoint) == Velocity2D:
            self.x += otherPoint.x
            self.y += otherPoint.y
        else:
            raise Exception

    def add_calc(self, otherPoint):
        return Point2D(self.x + otherPoint.x, self.y + otherPoint.y)


# for testing purposes
if __name__ == "__main__":
    p = Point2D()
    p2 = Point2D()
    p.add_update(p2)