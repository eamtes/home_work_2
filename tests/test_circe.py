from src.circle import Circle
import pytest

test_c = Circle(10)
PI = 3.141592653589793


def test_circle_area():
    test_formula = PI * test_c.radius ** 2
    assert test_formula == test_c.area


def test_circle_perimeter():
    test_formula = 2 * PI * test_c.radius
    assert test_formula == test_c.perimeter


def test_circle_add_area():
    circle_add_area = test_c.add_area(test_c)
    assert circle_add_area == test_c.area * 2


def test_circle_add_area_raise():
    with pytest.raises(ValueError):
        test_c.add_area(1)
