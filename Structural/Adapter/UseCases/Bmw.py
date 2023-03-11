from Bmw_interface import IBmw


class Bmw(IBmw):

    def __init__(self):
        self.tires: int = 0
        self.model: str = ''
        self.color: str = ''

    def manufacture(self, model: str, color: str, tires: int):
        self.color = color
        self.model = model
        self.tires = tires

    def __str__(self):
        return f"Bmw: {self.model} {self.color} {self.tires}"
