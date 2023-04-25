from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """
    The builder interface
    """

    @staticmethod
    @abstractmethod
    def build_part_one():
        """
        Build first part
        """

    @staticmethod
    @abstractmethod
    def build_part_two():
        """
        Build second part
        """

    @staticmethod
    @abstractmethod
    def build_part_three():
        """
        Build third part
        """

    @staticmethod
    @abstractmethod
    def get_result():
        """
        Return the final product
        """
