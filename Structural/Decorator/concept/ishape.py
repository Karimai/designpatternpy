from abc import ABC


class IShape(ABC):
    def __str__(self):
        pass


class Circle(IShape):
    def __init__(self, radius = 0):
        self.radius = radius

    def __str__(self):
        return f"A circle of radius {self.radius}"

    def resize(self, factor: float):
        self.radius *= factor


class Square(IShape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A Square with side {self.side}"


class ColoredShape(IShape):
    def __init__(self, shape: IShape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(IShape):
    def __init__(self, shape: IShape, transparency: float):
        self.shape = shape
        self.trnsparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.trnsparency * 100.0}% transparency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "Red")
    print(red_circle)

    transparent_circle = TransparentShape(circle, 0.50)
    print(transparent_circle)
