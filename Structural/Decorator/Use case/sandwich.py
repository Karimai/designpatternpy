from sandwich_interface import ISandwich


class Sandwich(ISandwich):
    def __init__(self, bread: str, meat: str, cheese: str):
        self.bread: str = bread
        self.meat: str = meat
        self.cheese: str = cheese

    def get_sandwich(self):
        return f"{self.bread} bread, {self.meat} meat, {self.cheese} cheese"
