"""
A Leaderboard Singleton Class
"""
import threading


class Leaderboard:
    """
    The Leaderboard as a Singleton
    """

    _table = {}
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                """
                It's generally considered good practice to use
                super().__new__(cls) to ensure that the instance
                is properly initialized.
                """
                cls._instance = super().__new__(cls)
            return cls._instance

    @classmethod
    def print(cls):
        print("-----------------board-----------------")
        for name, position in sorted(cls._table.items()):
            print(f"{name}\t\t{position}")
        print("--------")

    @classmethod
    def add_winner(cls, name, position):
        """
        A class level method
        """
        cls._table[position] = name
