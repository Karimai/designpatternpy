from abc import ABCMeta, abstractmethod
from first_factory import FactoryA
from second_factory import FactoryB


class IAbstractFactory(metaclass=ABCMeta):
    """
    Abstract Factory
    """

    @staticmethod
    @abstractmethod
    def create_object(factory):
        """
        The static Abstract Factory method
        """


class AbstractFactory(IAbstractFactory):
    @staticmethod
    def create_object(factory):
        if factory in ["a", "b", "c"]:
            return FactoryA.create_object(factory)
        if factory in ["d", "e"]:
            return FactoryB.create_object(factory)
        return None


for prod_type in ["a", "d", "e"]:
    prod = AbstractFactory.create_object(prod_type)
    print(prod.__class__)
