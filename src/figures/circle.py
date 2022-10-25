import math

from src import Figure


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.name = 'Circle'

    @property
    def perimeter(self):
        return round((2 * math.pi * self.r), 2)

    @property
    def area(self):
        return round((math.pi * (self.r ** 2)), 2)
