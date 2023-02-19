from table_interface import ITable


class CircleTable(ITable):

    def __init__(self):
        self._horizontal_radius = 50
        self._vertical_radius = 50

    def get_dimentions(self):
        return {
            'horizontal_radius': self._horizontal_radius,
            'vertical_radius': self._vertical_radius
        }
