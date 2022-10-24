import random

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


import pytest

square = square(a=random.randint(3, 9))


def test_square_name():
    name = square.name
    assert name == 'Square', 'Неверное наименование фигуры'


def test_square_perimeter():
    perimeter = square.perimeter
    assert perimeter == 4 * square.a, 'Неверно рассчитан периметр'


def test_square_area():
    area = square.area
    assert area == square.a ** square.a, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(a=1, b=2), circle(r=4), square, triangle(1, 2, 3)])
def test_square_add_area(figure):
    sum_area = square.add_area(figure)
    assert sum_area == square.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_square_add_incorrect_area():
    try:
        square.add_area('123')
    except ValueError:
        assert True
