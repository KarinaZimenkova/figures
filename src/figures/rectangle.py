from src import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = 'Rectangle'

        if self.a == self.b:
            self.name = 'Square'

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b
