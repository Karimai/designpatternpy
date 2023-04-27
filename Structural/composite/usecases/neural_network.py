from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    """
    A singular element, scalar element
    A scalar element is a single value that cannot be subdivided into smaller components.
    Scalars are typically used to represent basic data types.
    """

    def __init__(self, name: str):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self):
        """
        Make it iterable!
        """
        yield self

    def __str__(self):
        return f"{self.name}, {len(self.inputs)} inputs and {len(self.outputs)} outputs"


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f"{self.name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    neuron1 = Neuron("N1")
    neuron2 = Neuron("N2")
    layer1 = NeuronLayer("L1", 3)
    layer2 = NeuronLayer("L2", 4)

    neuron1.connect_to(neuron2)
    neuron2.connect_to(neuron1)
    layer1.connect_to(layer2)
    layer2.connect_to(layer1)

    print(neuron1)
    print(neuron2)
