class ConcreteFlyweight:
    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str):
        print(f"Concrete FlyWeight: {self._intrinsic_state}, {extrinsic_state}")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key: str):
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
