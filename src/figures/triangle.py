from math import sqrt

from src.figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'
        if self.a + self.b < self.c \
                or self.a + self.c < self.b \
                or self.c + self.b < self.a:
            raise ValueError
    
    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter/2
        h = (2 / self.a) * sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return round(0.5 * self.a * h, 2)

