from abc import ABCMeta, abstractmethod


class IFlyweight(metaclass=ABCMeta):
    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class Flyweight(IFlyweight):
    def __init__(self, intrinsic_state):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"Concrete FlyWeight: {self._intrinsic_state}, {extrinsic_state}")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight(key)
        return self._flyweights[key]


factory = FlyweightFactory()

first_flyweight = factory.get_flyweight("key_1")
first_flyweight.operation("A")

second_flyweight = factory.get_flyweight("key_2")
second_flyweight.operation("B")

first_flyweight = factory.get_flyweight("key_1")
first_flyweight.operation("C")
