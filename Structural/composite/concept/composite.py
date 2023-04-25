from component_interface import IComponent


class Composite(IComponent):
    def __init__(self, name: str, investment: int):
        super().__init__(name, investment)
        self.total_invest = investment
        self.leaves = []

    def status(self):
        for leaf in self.leaves:
            leaf.status()
        print(
            f"Name:{self._name}, "
            f"Investment: {self._investment}, "
            f"Total Investment:{self.total_invest}"
        )

    def add(self, investor: IComponent):
        self.leaves.append(investor)
        self.total_invest += investor._investment

    def remove(self, investor: IComponent):
        self.leaves.remove(investor)
        self.total_invest -= investor._investment
