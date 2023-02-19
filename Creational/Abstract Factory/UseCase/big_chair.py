from chair_interface import IChair


class BigChair(IChair):

    def __init__(self):
        self._height: int = 60
        self._width: int = 100
        self._depth: int = 70

    def get_dimentions(self) -> dict[str, int]:
        return {
            'width': self._width,
            'height': self._height,
            'depth': self._depth
        }