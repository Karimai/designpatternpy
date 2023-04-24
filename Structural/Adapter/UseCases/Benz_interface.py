from abc import ABCMeta, abstractmethod


class IBenz(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create(model, tires, color):
        pass
