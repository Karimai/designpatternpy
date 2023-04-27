from abc import ABC, abstractmethod


class IRenderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        """"""


class VectorRenderer(IRenderer):
    def render_circle(self, radius):
        print(f"Drawing a circle for of radius {radius}")


class RasterRenderer(IRenderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for circle of radius {radius}")


class Shape:
    def __init__(self, renderer: IRenderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor: int):
        pass


class Circle(Shape):
    def __init__(self, renderer: IRenderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: int):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circles = [Circle(vector, 5), Circle(raster, 5)]
    for circle in circles:
        circle.draw()
        circle.resize(3)
        circle.draw()
