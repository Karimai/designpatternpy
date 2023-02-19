from furniture_factory import FurnitureFactory

furniture = FurnitureFactory.get_furniture('big Chair')
print(f'{furniture.__class__}:{furniture.get_dimentions()}')

furniture = FurnitureFactory.get_furniture('rectangle Table')
print(f'{furniture.__class__}:{furniture.get_dimentions()}')
