from chair_factory import ChairFactory

chair_type = input("which chair type(big, small, or medium):")

chair = ChairFactory.get_chair(chair_type)

print("the dimensions of the requested chair:", chair.get_dimensions())
