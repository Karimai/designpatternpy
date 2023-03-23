from abc import ABC, abstractmethod


class IShape(ABC):

    @staticmethod
    @abstractmethod
    def draw():
        pass
