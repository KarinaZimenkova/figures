import pytest
import random

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


def test_rectangle_name(new_rectangle):
    r_name = new_rectangle.name
    assert r_name == 'Rectangle', 'Неверное наименование фигуры'


def test_rectangle_perimeter(new_rectangle):
    r_perimeter = new_rectangle.perimeter
    assert r_perimeter == 2 * (new_rectangle.a + new_rectangle.b), 'Неверно рассчитан периметр'


def test_rectangle_area(new_rectangle):
    r_area = new_rectangle.area
    assert r_area == new_rectangle.a * new_rectangle.b, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [circle(r=4), square(a=3), triangle(a=1, b=2, c=3)])
def test_rectangle_add_area(figure, new_rectangle):
    sum_area = new_rectangle.add_area(figure)
    assert sum_area == new_rectangle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_rectangle_add_incorrect_area(new_rectangle):
    try:
        new_rectangle.add_area('123')
    except ValueError:
        assert True


def test_rectangle_is_square(new_rectangle):
    _square = rectangle(a=new_rectangle.a, b=new_rectangle.a)
    square_name = _square.name
    assert square_name == 'Square', 'Неверное наименование фигуры'


@pytest.fixture()
def new_rectangle():
    return rectangle(a=random.randint(1, 5), b=random.randint(6, 9))
