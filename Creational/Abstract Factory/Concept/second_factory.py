from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create_object():
        """
        A Class that implements the IProduct
        """


class ProductA(IProduct):
    """
    A Class that implements the IProduct
    """

    def __init__(self):
        self.name = "Product A"

    def create_object(self):
        return self


class ProductB(IProduct):
    """
    A Class that implements the IProduct
    """

    def __init__(self):
        self.name = "Product B"

    def create_object(self):
        return self


class FactoryB:

    @staticmethod
    def create_object(product_type: str):
        if product_type == 'd':
            return ProductA()
        if product_type == 'e':
            return ProductB()
        return None
