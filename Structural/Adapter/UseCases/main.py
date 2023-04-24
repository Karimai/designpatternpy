import random

from Benz import Benz
from Benz_adaptor import BenzAdaptor
from Bmw import Bmw

if __name__ == "__main__":
    for i in range(5):
        if random.choice([True, False]):
            car = Benz()
            models = ["A-Klasse", "GLC", "GLE"]
        else:
            car = BenzAdaptor(Bmw())
            models = ["X", "G", "Luxury"]

        car.create(
            model=random.choice(models),
            tires=random.choice([4, 6]),
            color=random.choice(["white", "blue", "gray"]),
        )

        print(car)
