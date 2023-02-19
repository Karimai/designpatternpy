from chair_interface import IChair


class SmallChair(IChair):

    def __init__(self):
        self._height: int = 120
        self._width: int = 55
        self._depth : int = 60

    def get_dimentions(self) -> dict[str, int]:
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
