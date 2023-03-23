from abc import ABC, abstractmethod


class IShapeImplementer(ABC):
    """
    Shape implementer interface
    """

    @staticmethod
    @abstractmethod
    def draw_implementation():
        pass
    