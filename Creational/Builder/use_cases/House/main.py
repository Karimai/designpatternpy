from builder import Builder
from director import Director

builder = Builder()
director = Director(builder)
house = director.build_house()

print(house.__dict__)
