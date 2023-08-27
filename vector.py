import math


class Vector:

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def str_(self) -> str:
        return "({},{},{})".format(self.x, self.y, self.z)

    def inner_product(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z*other.z

    def modulo(self, ) -> float:
        return math.sqrt(self.inner_product(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k: float):
        assert not isinstance(k, Vector)
        return Vector(self.x*k, self.y*k, self.z*k)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)

    def normalize(self):
        return self / self.modulo()


v1 = Vector(2, 3, 4)
v2 = Vector(1, 2, 5)
v3 = v1.sum(v2)
print(v1.normalize())
print(v3.str_())
