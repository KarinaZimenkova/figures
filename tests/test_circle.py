import math
import random
import pytest

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


def test_circle_name(new_circle):
    name = new_circle.name
    assert name == 'Circle', 'Неверное наименование фигуры'


def test_circle_perimeter(new_circle):
    perimeter = new_circle.perimeter
    assert perimeter == round((2 * math.pi * new_circle.r), 2), 'Неверно рассчитан периметр'


def test_circle_area(new_circle):
    area = new_circle.area
    assert area == round((math.pi * (new_circle.r ** 2)), 2), 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(a=1, b=2), square(a=3), triangle(a=1, b=2, c=3)])
def test_circle_add_area(figure, new_circle):
    sum_area = new_circle.add_area(figure)
    assert sum_area == new_circle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_circle_add_incorrect_area(new_circle):
    try:
        new_circle.add_area('123')
    except ValueError:
        assert True


@pytest.fixture()
def new_circle():
    return circle(r=random.randint(3, 9))
