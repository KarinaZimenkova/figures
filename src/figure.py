
class Figure:

    @property
    def area(self):
        return 0

    def add_area(self, figure):
        try:
            return self.area + figure.area
        except AttributeError:
            raise ValueError
