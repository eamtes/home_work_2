from src.rectangle import Rectangle
import pytest

test_r = Rectangle(12, 20)


def test_rectangle_area():
    test_formula = test_r.side_a * test_r.side_b
    assert test_formula == test_r.area


def test_rectangle_perimeter():
    test_formula = 2 * (test_r.side_a + test_r.side_b)
    assert test_formula == test_r.perimeter


def test_rectangle_add_area():
    rectangle_add_area = test_r.add_area(test_r)
    assert rectangle_add_area == test_r.area * 2


def test_rectangle_add_area_raise():
    with pytest.raises(ValueError):
        test_r.add_area(1)
