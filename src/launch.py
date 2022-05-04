from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


if __name__ == '__main__':
    square = Square(10)
    print(square.area)

    triangle = Triangle(13, 14, 15)
    print(triangle.area)

    circle = Circle(10)
    print(circle.area)

    rectangle = Rectangle(20, 15)
    print(rectangle.area)

    print(triangle.add_area(square))
    print(square.add_area(circle))
    print(circle.add_area(rectangle))
    print(rectangle.add_area(square))
