from abc import ABCMeta, abstractmethod


class IFlower(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method():
        "A method to implement"


class Flower(IFlower):
    def method(self):
        return "Flower"


class FlowerDecorator(IFlower):
    def __init__(self, obj):
        self.obj = obj

    def method(self):
        return f"A decorated {self.obj.method()}!"


if __name__ == "__main__":
    flower = Flower()
    print(flower.method())

    print(FlowerDecorator(flower).method())
