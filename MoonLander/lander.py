from Point2D import Point2D
from Velocity2D import Velocity2D

THRUST_POWER = 0.3
TOTAL_FUEL = 100
FUEL_COST = 1

class Lander:
    def __init__(self
                , position : Point2D = Point2D()
                , velocity : Velocity2D = Velocity2D()) -> None:
        self.position = position
        self.velocity = velocity
        self.fuel = TOTAL_FUEL
        self.crashed = False

    def thrust_down(self, time = 1) -> None:
        if self.fuel >= FUEL_COST * 3:
            self.fuel -= FUEL_COST * 3
            self.velocity.add_update(Velocity2D(0, -THRUST_POWER * time))

    def thrust_left(self, time = 1) -> None:
        if self.fuel >= FUEL_COST:
            self.fuel-=1
            self.velocity.add_update(Velocity2D(THRUST_POWER * time, 0))

    def thrust_right(self, time = 1) -> None:
        if self.fuel >= FUEL_COST:
            self.fuel-=1
            self.velocity.add_update(Velocity2D(-THRUST_POWER * time, 0))

    def display_lander(self) -> None:
        pass

    def apply_gravity(self, gravity_power, time = 1) -> None:
        self.velocity.add_update(Velocity2D(0, -gravity_power * time))

    def has_crashed(self) -> bool:
        return 
    
    def has_fuel(self) -> bool:
        return self.fuel > 0

    def apply_physics(self) -> None:
        self.position.add_update(self.velocity)