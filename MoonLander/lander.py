from Point2D import Point2D
from Velocity2D import Velocity2D

THRUST_POWER = 0.3

class Lander:
    def __init__(self
                , position : Point2D = Point2D()
                , velocity : Velocity2D = Velocity2D()) -> None:
        self.position = position
        self.velocity = velocity
        self.fuel = 100
        self.crashed = False

    def thrust_down(self, time = 1) -> None:
        self.velocity.add_update(Velocity2D(0, THRUST_POWER * time))

    def thrust_left(self, time = 1) -> None:
        self.velocity.add_update(Velocity2D(THRUST_POWER * time, 0))

    def thrust_right(self, time = 1) -> None:
        self.velocity.add_update(Velocity2D(-THRUST_POWER * time, 0))

    def display_lander(self) -> None:
        pass

    def apply_gravity(self, gravity_power, time = 1) -> None:
        self.velocity.add_update(Velocity2D(0, -gravity_power * time))

    def has_crashed(self) -> bool:
        return 
    
    def has_fuel(self) -> bool:
        return self.fuel > 0