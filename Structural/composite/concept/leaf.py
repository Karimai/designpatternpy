from component_interface import IComponent


class Leaf(IComponent):

    def status(self):
        print(f"Name: {self._name}, investment: {self._investment}")
