"""
A Leaderboard Singleton Class
"""


class Leaderboard:
    """
    The Leaderboard as a Singleton
    """
    _table = {}
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            '''
            It's generally considered good practice to use 
            super().__new__(cls) to ensure that the instance 
            is properly initialized.
            '''
            cls._instance = super().__new__(cls)
        return cls._instance

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
