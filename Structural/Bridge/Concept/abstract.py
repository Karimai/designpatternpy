from implementation_interface import IImplementation


class Abstraction:
    def __init__(self, implementation: IImplementation):
        self.implementation = implementation

    def operation(self):
        return self.implementation.operation_implementation()
