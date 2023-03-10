import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self, name: str = 'Unknown', color: str = 'Unknown', price: int = 0):
        self.name: str = name
        self.color: str = color
        self.price: int = price

    def __str__(self):
        return f"{self.name} | {self.color} | {self.price}"


car = Car('Toyota Corolla', 'Blue', 15000)

prototype = Prototype()
prototype.register_object('car', car)

car_clone = prototype.clone('car')
print(car_clone)


car_clone.name = 'Honda Civic'
car_clone.color = 'Red'
car_clone.price = 20000

print(car_clone)
