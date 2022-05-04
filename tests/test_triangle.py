import math
from src.triangle import Triangle
import pytest

test_t = Triangle(20, 15, 10)


def test_triangle_area():
    test_semi_perimeter = test_t.perimeter / 2
    test_formula = math.sqrt(test_semi_perimeter
                                * (test_semi_perimeter - test_t.side_a)
                                * (test_semi_perimeter - test_t.side_b)
                                * (test_semi_perimeter - test_t.side_c))
    assert test_formula == test_t.area


def test_triangle_perimeter():
    test_formula = test_t.side_a + test_t.side_b + test_t.side_c
    assert test_formula == test_t.perimeter


def test_triangle_add_area():
    triangle_add_area = test_t.add_area(test_t)
    assert triangle_add_area == test_t.area * 2


def test_triangle_add_area_raise():
    with pytest.raises(ValueError):
        test_t.add_area(1)
