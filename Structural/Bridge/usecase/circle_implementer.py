import pyfiglet
from shape_implementer_interface import IShapeImplementer


class CircleImplementer(IShapeImplementer):
    """
    A Circle Implementer
    """

    def draw_implementation(self):
        txt = pyfiglet.figlet_format("o", font="block")
        print(txt)
