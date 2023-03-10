import random
import threading
from leaderboard import Leaderboard
from first_game import Game

teams = ['Fc-byirn',
         'Ajax',
         'Dortmond',
         'Barca',
         'Real',
         'Milan',
         'Manchester',
         'Boka',
         'Pirozi',
         'Al Nasr']
ranks = [i for i in range(1, 11)]

random.shuffle(teams)
random.shuffle(ranks)


def games_runner(team: str, rank: int):

    game = Game()
    game.add_winner(team, rank)


threads = []

for team, rank in zip(teams, ranks):
    t = threading.Thread(target=games_runner(team, rank))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

board = Leaderboard()
board.print()
