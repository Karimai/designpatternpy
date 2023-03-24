from abc import ABCMeta, abstractmethod


class IFlyweight(metaclass=ABCMeta):
    @abstractmethod
    def operation(self, extrinsic_state):
        pass

