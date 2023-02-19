from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        """
        An obligatory method which should be implemented
        """