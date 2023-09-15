from typing import Callable

from Point2D import Point2D
from Velocity2D import Velocity2D

CHARACTER_WIDTH: int    = 64
CHARACTER_OFFSET: int   = CHARACTER_WIDTH // 2
THRUST_POWER: float     = 0.3
TOTAL_FUEL: int         = 100
FUEL_COST: int          = 1


class Lander:
    def __init__(self
                , position: Point2D = Point2D()
                , velocity: Velocity2D = Velocity2D()) -> None:
        self.position = position
        self.velocity = velocity
        self.fuel = TOTAL_FUEL
        self.crashed = False

    def thrust_down(self, time: int = 1) -> None:
        if self.fuel >= FUEL_COST * 3 and not self.crashed:
            self.fuel -= FUEL_COST * 3
            self.velocity.add_update(Velocity2D(0, -THRUST_POWER * time))

    def thrust_left(self, time: int = 1) -> None:
        if self.fuel >= FUEL_COST and not self.crashed:
            self.fuel-=1
            self.velocity.add_update(Velocity2D(THRUST_POWER * time, 0))

    def thrust_right(self, time: int = 1) -> None:
        if self.fuel >= FUEL_COST and not self.crashed:
            self.fuel-=1
            self.velocity.add_update(Velocity2D(-THRUST_POWER * time, 0))

    def display_lander(self, callback_display_function: Callable) -> None:
        # Display from the center of the sprite
        callback_display_function(Point2D(self.position.x - CHARACTER_OFFSET, self.position.y - CHARACTER_OFFSET))

    def apply_gravity(self, gravity_power, time = 1) -> None:
        self.velocity.add_update(Velocity2D(0, -gravity_power * time))

    def has_crashed(self) -> bool:
        return self.crashed
    
    def has_fuel(self) -> bool:
        return self.fuel > 0

    def apply_physics(self) -> None:
        self.position.add_update(self.velocity)