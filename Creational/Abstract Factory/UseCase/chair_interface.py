from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimentions() -> dict[str, int]:
        """
        No need implementation in interface
        """
