from point import Point
from vector import Vector


class Cam:
    location: Point
    aim: Point
    Vup: Vector
    W: Vector
    U: Vector
    V: Vector

    screen_heigth: float
    screen_width: float
    screen_distance: float


    def __init__(self) -> None:
        pass