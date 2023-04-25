from abc import ABCMeta, abstractmethod


class ISandwich(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_sandwich():
        """
        return properties of a sandwich
        """
