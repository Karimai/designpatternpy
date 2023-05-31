from table_circle import CircleTable
from table_interface import ITable
from table_rectangle import RectangleTable


class TableFactory:
    @staticmethod
    def get_table(table_type: str) -> ITable | None:
        if "circle" in table_type.lower():
            return CircleTable()
        if "rectangle" in table_type.lower():
            return RectangleTable()
        return None
