from abc import ABC


class Renderer(ABC):
    @property
    def render_as(self):
        return None


class Shape:
    def __init__(self, renderer: Renderer, name: str):
        self.name = name
        self.renderer = renderer

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.render_as}"


class Triangle(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer, self.__class__.__name__)


class Square(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer, self.__class__.__name__)


class VectorRenderer(Renderer):
    @property
    def render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def render_as(self):
        return "pixels"


def test_square_vector():
    assert str(Square(VectorRenderer())) == "Drawing Square as lines"
    assert str(Triangle(VectorRenderer())) == "Drawing Triangle as lines"
    assert str(Square(RasterRenderer())) == "Drawing Square as pixels"
    assert str(Triangle(RasterRenderer())) == "Drawing Triangle as pixels"
