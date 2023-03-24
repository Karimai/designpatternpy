
from flyweight_interface import IFlyweight


class Flyweight(IFlyweight):
    def __init__(self, intrinsic_state):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        pass


