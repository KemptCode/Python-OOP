from Point2D import Point2D
from Velocity2D import Velocity2D

THRUST_POWER = 0.3

class Lander:
    def __init__(self
                , position : Point2D = Point2D()
                , velocity : Velocity2D = Velocity2D()) -> None:
        self.position = position
        self.velocity = velocity

    def thrust_down(self, time = 1):
        pass

    def thrust_left(self, time = 1):
        pass

    def thrust_right(self, time = 1):
        pass

    def display_lander(self):
        pass

    def apply_gravity(self, gravity_power):
        pass