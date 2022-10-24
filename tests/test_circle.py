import math
import random
import pytest

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle

circle = circle(r=random.randint(3, 9))


def test_circle_name():
    name = circle.name
    assert name == 'Circle', 'Неверное наименование фигуры'


def test_circle_perimeter():
    perimeter = circle.perimeter
    assert perimeter == round((2 * math.pi * circle.r), 2), 'Неверно рассчитан периметр'


def test_circle_area():
    area = circle.area
    assert area == round((math.pi * (circle.r ** 2)), 2), 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(1, 2), circle, square(3), triangle(1, 2, 3)])
def test_circle_add_area(figure):
    sum_area = circle.add_area(figure)
    assert sum_area == circle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_circle_add_incorrect_area():
    try:
        circle.add_area('123')
    except ValueError:
        assert True
