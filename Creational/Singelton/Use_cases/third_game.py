from leaderboard import Leaderboard
from game_interface import IGame


class ThirdGame(IGame):

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, name, position):
        self.leaderboard.add_winner(name, position)
