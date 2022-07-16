class Velocity2D:
    '''

    '''
    def __init__(self, dx = 0, dy = 0) -> None:
        self.dx = dx
        self.dy = dy

    def add_update(self, otherVel):
        if type(otherVel) == Velocity2D:
            self.dx += otherVel.dx
            self.dy += otherVel.dy
        else:
            raise Exception

    def add_calc(self, otherVel):
        return Velocity2D(self.dx + otherVel.dx, self.dy + otherVel.dy)

# for testing purposes only
if __name__ == "__main__":        
    v = Velocity2D()
    v2 = Velocity2D()
    v.add_update(v2)