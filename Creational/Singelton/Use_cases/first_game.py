"""
A Game Class that uses the leaderboard Singleton
"""

from game_interface import IGame
from leaderboard import Leaderboard


class FirstGame(IGame):
    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, name, position):
        self.leaderboard.add_winner(name, position)
