from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    """
    A Hypothetical Class Interface
    """

    @staticmethod
    @abstractmethod
    def create_object():
        """
        An Abstract method
        """


class ProductA(IProduct):
    """
    A class that implements the IProduct interface
    """

    def __init__(self):
        self.name = "Product A"

    def create_object(self):
        return self


class ProductB(IProduct):
    def __init__(self):
        self.name = "Product B"

    def create_object(self):
        return self


class FactoryA:
    @staticmethod
    def create_object(properties):
        try:
            if properties == "a":
                return ProductA()
            if properties == "b":
                return ProductB()
        except Exception as e:
            print(e)
        return None
