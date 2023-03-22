from abc import ABCMeta, abstractmethod


class IImplementation(metaclass=ABCMeta):
    @abstractmethod
    def operation_implementation(self):
        pass
