import random

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


import pytest


def test_square_name(new_square):
    name = new_square.name
    assert name == 'Square', 'Неверное наименование фигуры'


def test_square_perimeter(new_square):
    perimeter = new_square.perimeter
    assert perimeter == 4 * new_square.a, 'Неверно рассчитан периметр'


def test_square_area(new_square):
    area = new_square.area
    assert area == new_square.a ** 2, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(a=1, b=2), circle(r=4), triangle(1, 2, 3)])
def test_square_add_area(figure, new_square):
    sum_area = new_square.add_area(figure)
    assert sum_area == new_square.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_square_add_incorrect_area(new_square):
    try:
        new_square.add_area('123')
    except ValueError:
        assert True


@pytest.fixture()
def new_square():
    return square(a=random.randint(3, 9))
