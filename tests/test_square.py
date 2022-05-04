from src.square import Square
import pytest

test_s = Square(20)


def test_square_area():
    test_formula = test_s.side_length ** 2
    assert test_formula == test_s.area


def test_square_perimeter():
    test_formula = 4 * test_s.side_length
    assert test_formula == test_s.perimeter


def test_square_add_area():
    square_add_area = test_s.add_area(test_s)
    assert square_add_area == test_s.area * 2


def test_square_add_area_raise():
    with pytest.raises(ValueError):
        test_s.add_area(1)
