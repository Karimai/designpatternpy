from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    def __init__(self, name: str, investment: int):
        self._name = name
        self._investment = investment

    def status(self):
        pass

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def investment(self):
        return self._investment

    @investment.setter
    def investment(self, value: int):
        self._investment = value
