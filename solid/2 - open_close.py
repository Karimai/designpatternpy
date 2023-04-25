"""
Open for extension, close for modification
It suggests when you add a new functionality, you will add by extension,
not by modification.
After you add and test a function, you can not modify it further
"""
from dataclasses import dataclass
from enum import Enum
from typing import List


class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


@dataclass
class Product:
    name: str
    color: Color
    size: Size


class ProductFilter:
    # the basic implementation. It only has filter by color
    @staticmethod
    def filter_by_color(prods: List[Product], color: Color):
        # for p in products:
        #     if p.color == color:
        #         yield p
        return filter(lambda pr: pr.color == color, prods)

    # according to a new feature request, a filter_by_size should be added
    # So, ok, we add another filter by size
    @staticmethod
    def filter_by_size(prods: List[Product], size: Size):
        # for p in products:
        #     if p.size == size:
        #         yield p
        return filter(lambda pr: pr.size == size, prods)

    @staticmethod
    def filter_by_color_size(prods: List[Product], color: Color, size: Size):
        # for p in products:
        #     if p.color == color and p.size == size:
        #         yield p
        return filter(lambda pr: pr.color == color and pr.size == size, prods)


apple = Product("Apple", Color.Green, Size.SMALL)
tree = Product("Tree", Color.Green, Size.LARGE)
house = Product("House", Color.Blue, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
for p in pf.filter_by_color(products, Color.Green):
    print(f" - {p.name} is green!")

for p in pf.filter_by_size(products, Size.LARGE):
    print(f" - {p.name} is large!")

# ################################# Applying OCP ###########
print("############ OCP #############")


class Specification:
    def is_satisfied(self, other):
        pass

    # override the `and` operator!
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class OCPFilter(Filter):
    def filter(self, items, spec):
        # for item in items:
        #     if spec.is_satisfied(item):
        #         yield item
        return filter(spec.is_satisfied, items)


ocp_filter = OCPFilter()

print("Green products:")
green = ColorSpecification(Color.Green)
for p in ocp_filter.filter(products, green):
    print(f" - {p.name} is green!")

print("Large products:")
large = SizeSpecification(Size.LARGE)
for p in ocp_filter.filter(products, large):
    print(f" - {p.name} is large!")

print("Large Blue items")
blue = ColorSpecification(Color.Blue)
large_blue = large & blue
for p in ocp_filter.filter(products, large_blue):
    print(f"  - {p.name} is large and blue")
