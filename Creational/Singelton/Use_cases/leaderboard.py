"""
A Leaderboard Singleton Class
"""


class Leaderboard:
    """
    The Leaderboard as a Singleton
    """
    _table = {}

    def __new__(cls, *args, **kwargs):
        return cls

    @classmethod
    def print(cls):
        print('-----------------board-----------------')
        for name, position in sorted(cls._table.items()):
            print(f"{position}\t\t{name}")
        print()

    @classmethod
    def add_winner(cls, name, position):
        """
        A class level method
        """
        cls._table[position] = name
