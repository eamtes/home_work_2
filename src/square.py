from src.figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def area(self):
        return self.side_length ** 2

    @property
    def perimeter(self):
        return 4 * self.side_length
