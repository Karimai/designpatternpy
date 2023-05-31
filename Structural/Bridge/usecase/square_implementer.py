import pyfiglet
from shape_implementer_interface import IShapeImplementer


class SquareImplementer(IShapeImplementer):
    def draw_implementation(self):
        txt = pyfiglet.figlet_format("o", font="isometric3")
        print(txt)
