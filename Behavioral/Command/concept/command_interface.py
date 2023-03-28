from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

