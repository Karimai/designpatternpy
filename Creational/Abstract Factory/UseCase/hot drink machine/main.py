from abc import ABC
from enum import Enum, auto


class IHotDrink(ABC):
    def consume(self):
        pass


class Tea(IHotDrink):
    def consume(self):
        print("Drink your tea!")


class Coffee(IHotDrink):
    def consume(self):
        print("Drink your coffee!")


class IHotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(IHotDrinkFactory):
    def prepare(self, amount):
        print(f"put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(IHotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}): ")
        idx = int(s)
        s = input("How much strong: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hot_drink_machine = HotDrinkMachine()
    drink = hot_drink_machine.make_drink()
    drink.consume()
