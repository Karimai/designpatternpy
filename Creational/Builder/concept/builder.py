from builder_interface import IBuilder
from product import Product


class Builder(IBuilder):
    """
    The Builder class
    """
    def __init__(self):
        self.product = Product()

    def build_part_one(self):
        self.product.parts.append('1')
        return self

    def build_part_two(self):
        self.product.parts.append('2')
        return self

    def build_part_three(self):
        self.product.parts.append('3')
        return self

    def get_result(self):
        return self.product
