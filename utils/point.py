class Point:
    x = None
    y = None
    z = None

    def __init__(self, x=0.0, y=0.0, z=0.0) -> None:
        assert x != None
        assert y != None
        assert z != None
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Poin({self.x}, {self.y}, {self.z})"