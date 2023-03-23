from shape_interface import IShape


class Square(IShape):
    """
    The Square is a refined abstraction
    """

    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()
