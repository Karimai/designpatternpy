from chair_factory import ChairFactory
from chair_interface import IChair
from furniture_factory_interface import IFurnitureFactory
from table_factory import TableFactory
from table_interface import ITable


class FurnitureFactory(IFurnitureFactory):
    @staticmethod
    def get_furniture(furniture: str) -> [ITable | IChair]:
        if "chair" in furniture.lower():
            return ChairFactory.get_chair(furniture)
        if "table" in furniture.lower():
            return TableFactory.get_table(furniture)
        return None
