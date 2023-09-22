from vector import Vector

class Color(Vector):
    def __init__(self, red: float, green: float, blue: float) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    @property
    def x(self):
        return self.red

    @property
    def y(self):
        return self.green

    @property
    def z(self):
        return self.blue

    def to_byte_map(self):
        def to_byte(value):
            return round(max(min(value * 255, 255), 0))
        return "{} {} {} ".format(
            to_byte(self.x),
            to_byte(self.y),
            to_byte(self.z)
        )

    def __str__(self):
        return f"Color ({self.red}, {self.green}, {self.blue})"