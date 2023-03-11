import random

from Benz_adaptor import BenzAdaptor
from Benz import Benz
from Bmw import Bmw

if __name__ == '__main__':
    for i in range(5):
        rnd = random.choice([True, False])

        if rnd:
            car = Benz()
            models = ['A-Klasse', 'GLC', 'GLE']
        else:
            car = BenzAdaptor(Bmw())
            models = ['X', 'G', 'Luxury']

        car.create(model=random.choice(models),
                   tires=random.choice([4, 6]),
                   color=random.choice(['white', 'blue', 'gray']))

        print(car)

