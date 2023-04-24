from abc import ABCMeta, abstractmethod


class IBmw(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def manufacture(model, color, tires):
        pass
