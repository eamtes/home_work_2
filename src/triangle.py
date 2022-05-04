import math
from src.figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        semi_perimeter = self.perimeter / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.side_a)
                         * (semi_perimeter - self.side_b)
                         * (semi_perimeter - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
