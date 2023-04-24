from Benz_interface import IBenz


class Benz(IBenz):
    def __init__(self):
        self.model = None
        self.tires = None
        self.color = None

    def create(self, model: str, tires: int, color: str):
        self.model = model
        self.tires = tires
        self.color = color

    def __str__(self):
        return f"Benz: {self.model} {self.color} {self.tires}"
