from abc import ABCMeta, abstractmethod


class IService(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def request():
        """
        It should be implemented in the instances
        """