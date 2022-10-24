import math
import pytest

from src.figures import Rectangle as rectangle
from src.figures import Circle as circle
from src.figures import Square as square
from src.figures import Triangle as triangle


corr_triangle = triangle(a=1, b=2, c=3)


def test_triangle_name():
    name = corr_triangle.name
    assert name == 'Triangle', 'Неверное наименование фигуры'


def test_triangle_perimeter():
    perimeter = corr_triangle.perimeter
    assert perimeter == corr_triangle.a + corr_triangle.b + corr_triangle.c, 'Неверно рассчитан периметр'


def test_triangle_area():
    fact_area = corr_triangle.area
    p = corr_triangle.perimeter / 2
    h = (2 / corr_triangle.a) * math.sqrt(p * (p - corr_triangle.a) * (p - corr_triangle.b) * (p - corr_triangle.c))
    exp_area = round(0.5 * corr_triangle.a * h, 2)
    assert fact_area == exp_area, 'Неверно рассчитана площадь'


@pytest.mark.parametrize("figure", [rectangle(1, 2), corr_triangle, square(3), circle(2)])
def test_triangle_add_area(figure):
    sum_area = corr_triangle.add_area(figure)
    assert sum_area == corr_triangle.area + figure.area, 'Неверно рассчитана площадь двух фигур'


def test_triangle_add_incorrect_area():
    try:
        corr_triangle.add_area('123')
    except ValueError:
        assert True


def test_figure_is_not_triangle():
    try:
        triangle(a=1, b=1, c=3)
    except ValueError:
        assert True
