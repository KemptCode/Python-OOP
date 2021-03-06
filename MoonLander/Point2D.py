from Velocity2D import Velocity2D

class Point2D:
    '''
    Holds the 2D position in x and y
    add_update  takes an Point2D or Velocity2D 
                and updates state of self
    add_calc    adds another Point2D 
                and returns value without updating state
    '''
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def add_update(self, otherPoint : "Point2D" | Velocity2D) -> None:
        if type(otherPoint) == Point2D:
            self.x += otherPoint.x
            self.y += otherPoint.y
        elif type(otherPoint) == Velocity2D:
            self.x += otherPoint.x
            self.y += otherPoint.y
        else:
            raise Exception

    def add_calc(self, otherPoint : "Point2D") -> "Point2D":
        return Point2D(self.x + otherPoint.x, self.y + otherPoint.y)


# for testing purposes only
if __name__ == "__main__":
    p = Point2D()
    p2 = Point2D()
    p.add_update(p2)