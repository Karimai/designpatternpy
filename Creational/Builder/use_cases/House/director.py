from builder_interface import IBuilder
from house import House


class Director:
    def __init__(self, builder: IBuilder):
        self.builder = builder

    def build_house(self) -> House:
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_door()
        self.builder.build_window()

        return self.builder.house
