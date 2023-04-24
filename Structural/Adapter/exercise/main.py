"""
You are given a class called Square and a function calculate_area() which calculates the area of a given rectangle.

In order to use Square in calculate_area, instead of augmenting it with width/height members, please implement the
SquareToRectangleAdapter class. This adapter takes a square and adapts it in such a way that it can be used as an
argument to calculate_area().
"""


class Square:
    def __init__(self, side=0):
        self.side = side


def cal_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square: Square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


def test_exercise():
    sq = Square(11)
    adapter = SquareToRectangleAdapter(sq)
    assert cal_area(adapter) == 121

    sq.side = 10
    assert cal_area(adapter) == 110
