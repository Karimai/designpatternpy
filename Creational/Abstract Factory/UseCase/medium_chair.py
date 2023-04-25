from chair_interface import IChair


class MediumChair(IChair):
    def __init__(self):
        self._height: int = 100
        self._width: int = 80
        self._depth: int = 60

    def get_dimentions(self) -> dict[str, int]:
        return {"width": self._width, "height": self._height, "depth": self._depth}
