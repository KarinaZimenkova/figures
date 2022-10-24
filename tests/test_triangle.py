import math
import pytest

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


def test_triangle_name(new_triangle):
    name = new_triangle.name
    assert name == 'Triangle', 'Неверное наименование фигуры'


def test_triangle_perimeter(new_triangle):
    perimeter = new_triangle.perimeter
    assert perimeter == new_triangle.a + new_triangle.b + new_triangle.c, 'Неверно рассчитан периметр'


def test_triangle_area(new_triangle):
    fact_area = new_triangle.area
    p = new_triangle.perimeter / 2
    h = (2 / new_triangle.a) * math.sqrt(p * (p - new_triangle.a) * (p - new_triangle.b) * (p - new_triangle.c))
    exp_area = round(0.5 * new_triangle.a * h, 2)
    assert fact_area == exp_area, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(1, 2), square(3), circle(2)])
def test_triangle_add_area(figure, new_triangle):
    sum_area = new_triangle.add_area(figure)
    assert sum_area == new_triangle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_triangle_add_incorrect_area(new_triangle):
    try:
        new_triangle.add_area('123')
    except ValueError:
        assert True


def test_figure_is_not_triangle():
    try:
        triangle(a=1, b=1, c=3)
    except ValueError:
        assert True


@pytest.fixture()
def new_triangle():
    return triangle(a=1, b=2, c=3)
