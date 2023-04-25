from flyweight_factory import FlyweightFactory

factory = FlyweightFactory()

first_flyweight = factory.get_flyweight("key_1")
first_flyweight.operation("A")

second_flyweight = factory.get_flyweight("key_2")
second_flyweight.operation("B")

first_flyweight = factory.get_flyweight("key_1")
first_flyweight.operation("C")
