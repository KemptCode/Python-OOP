class Velocity2D:
    '''

    '''
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def add_update(self, otherPoint):
        if type(otherPoint) == Velocity2D:
            self.x += otherPoint.x
            self.y += otherPoint.y
        else:
            raise Exception

    def add_calc(self, otherPoint):
        return Velocity2D(self.x + otherPoint.x, self.y + otherPoint.y)
        
v = Velocity2D()
v2 = Velocity2D()
v.add_update(v2)