class GraphicObject:
    def __init__(self, color: str | None = None):
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def depth_print(self, items, depth):
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"\t{self.name}\n")
        for child in self.children:
            child.depth_print(items, depth + 1)

    def __str__(self):
        items = []
        self.depth_print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing.name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))

    drawing.children.append(group)

    print(drawing)
