from circle import Circle
from circle_implementer import CircleImplementer
from square import Square
from square_implementer import SquareImplementer

shapes = [Circle(CircleImplementer), Square(SquareImplementer)]
for shape in shapes:
    shape.draw()
