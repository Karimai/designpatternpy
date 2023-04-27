from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    """
    It is the component!
    """
    @property
    def sum(self):
        return sum(i for c in self for i in c)


class SingleValue(ValueContainer):
    """
    It is the leaf!
    Represent a single value!
    """
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    """
    It is composite.
    Represent a collection of values.
    """
    pass


def test():
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    assert all_values.sum == 66
