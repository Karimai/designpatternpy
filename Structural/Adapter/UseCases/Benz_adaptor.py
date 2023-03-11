from Benz_interface import IBenz
from Bmw import Bmw


class BenzAdaptor(IBenz):
    """
    BenzAdaptor is an appropriate name since we'd like to adapt
    `Bmw` to conform to the Ibenz interface. It reflects the fact that
    the adapter is making a `Bmw` object compatible with the IBenz interface.
    """
    def __init__(self, bmw: Bmw):
        self.bmw = bmw

    def create(self, model, tires, color):
        self.bmw.manufacture(model=model, color=color, tires=tires)

    def __str__(self):
        return self.bmw.__str__()
