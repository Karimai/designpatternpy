from first_game import FirstGame
from second_game import SecondGame
from third_game import ThirdGame

Game_one = FirstGame()
Game_one.add_winner('Fc', 2)
Game_two = SecondGame()
Game_two.add_winner('Dort', 3)
Game_three = ThirdGame()
Game_three.add_winner('Barca', 1)

Game_one.leaderboard.print()
Game_two.leaderboard.print()
Game_three.leaderboard.print()
