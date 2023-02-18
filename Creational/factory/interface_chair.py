from abc import ABCMeta, abstractmethod

"""
# metaclass is a class that defines the behavior of other classes. When a
class is defined, Python creates an object that represents the class, which
is an instance of its metaclass. The metaclass can control how the class is
created, what attributes and methods is has, and how it behaves.
ABCMeta is short for Abstract Base Class.
This is a special metaclass in Python that allows you to define abstract
base classes (ABCs) that enforce certain rules on the classes that inherit
from them. An ABC class is a class that cannot be instantiated on its own,
but it provides a blueprint for other classes to follow.
IChair is a blueprint of a chair product.
"""


class IChair(metaclass=ABCMeta):
    """
    The chair interface
    """

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """
        abstractmethod means any class that inherited must provide an implementation of this method.
        A static interface method.
        :return: dictionary
        """
