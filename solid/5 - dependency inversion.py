"""
It is mainly for decoupling.
1) High-level modules should not depend on low-level modules.
    Both should depend on abstraction (e.g. interface) in between.
2) Abstractions should not depend on details.
    Details (concert implementation) should depend on abstraction.

High-level classes shouldn't have to change just because low-level classes changed.

Use the dependency inversion principle to make your code more robust by making the high-level module
depends on the abstraction, not the concrete implementation.

This makes our code more flexible and maintainable because we can easily switch out
the implementation of the interface base class without modifying the concrete user class.

The Dependency Inversion Principle is all about reducing coupling
 between modules in order to make code more flexible and maintainable.

In oop, coupling refers to the degree to which one class is dependent on another class.
When classes are tightly coupled, changes to one class can have a significant impact on the
other class, making the code more difficult to maintain and change.

By introducing an abstraction that both classes can depend on, we can decouple
the classes and make them more independent of each other. This makes it easier to change the
implementation of one class without affecting the other class, improving the overall flexibility
and maintainability of the codebase.
"""

from abc import ABC


class CurrencyConverter(ABC):

    def __init__(self):
        self.rate = 1.0

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        pass


class FXConverter(CurrencyConverter):
    def __init__(self):
        self.rate: float = 1.15

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        print('Converting currency using FX API')
        print(f"{amount} {from_currency} = {amount * self.rate} to {to_currency}")
        return amount * self.rate


class AlphaConverter(CurrencyConverter):
    def __init__(self):
        self.rate: float = 1.2

    def convert(self, from_currency: str, to_currency: str, amount: float) -> float:
        print("Converting currency using Alpha API")
        print(f"{amount} {from_currency} = {amount * self.rate} {to_currency}")
        return amount * self.rate


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def convert(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == "__main__":
    converter = AlphaConverter()
    app = App(converter)
    app.convert()

    app.converter = FXConverter()
    app.convert()


