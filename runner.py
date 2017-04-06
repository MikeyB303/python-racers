from die import Die
from python_racer import PythonRacer

die = Die(6)
players = ['a', 'b']
game = PythonRacer(players, die)

while True:

  game.board_visualization()
  game.advance_players()
