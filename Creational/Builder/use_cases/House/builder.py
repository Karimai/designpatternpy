from builder_interface import IBuilder
from house import House


class Builder(IBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "brick"

    def build_roof(self):
        self.house.roof = "slate"

    def build_door(self):
        self.house.doors = "wooden"

    def build_window(self):
        self.house.windows = "glass"
