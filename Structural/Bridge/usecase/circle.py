from shape_interface import IShape


class Circle(IShape):
    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()
