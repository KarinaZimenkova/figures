import pytest
import random

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


rectangle = rectangle(a=random.randint(1, 5), b=random.randint(6, 9))


def test_rectangle_name():
    r_name = rectangle.name
    assert r_name == 'Rectangle', 'Неверное наименование фигуры'


def test_rectangle_perimeter():
    r_perimeter = rectangle.perimeter
    assert r_perimeter == 2 * (rectangle.a + rectangle.b), 'Неверно рассчитан периметр'


def test_rectangle_area():
    r_area = rectangle.area
    assert r_area == rectangle.a * rectangle.b, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle, circle(r=4), square(a=3), triangle(a=1, b=2, c=3)])
def test_rectangle_add_area(figure):
    sum_area = rectangle.add_area(figure)
    assert sum_area == rectangle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_rectangle_add_incorrect_area():
    try:
        rectangle.add_area('123')
    except ValueError:
        assert True


def test_rectangle_is_square():
    _square = rectangle(a=rectangle.a, b=rectangle.a)
    square_name = _square.name
    assert square_name == 'Square', 'Неверное наименование фигуры'
