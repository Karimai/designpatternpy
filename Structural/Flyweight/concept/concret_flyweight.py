from flyweight import Flyweight


class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"Concrete FlyWeight: {self._intrinsic_state}, {extrinsic_state}")
