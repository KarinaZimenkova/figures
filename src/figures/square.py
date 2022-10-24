from src import Figure


class Square(Figure):

    def __init__(self, a):
        self.a = a
        self.name = 'Square'

    @property
    def perimeter(self):
        return 4 * self.a

    @property
    def area(self):
        return self.a ** 2
