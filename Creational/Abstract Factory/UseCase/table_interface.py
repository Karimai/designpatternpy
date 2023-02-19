from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimentions():
        """
        An obligatory table method
        """
