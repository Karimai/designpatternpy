"""A Game Interface"""

from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def add_winner(name, position):
        "Must be implemented"
