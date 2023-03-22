from first_implementation import FirstImplementation
from second_implementation import SecondImplemetation
from abstract import Abstraction

first_implementation = FirstImplementation()
second_implementation = SecondImplemetation()

abstractions = [Abstraction(first_implementation), Abstraction(second_implementation)]

for absts in abstractions:
    print(absts.operation())

