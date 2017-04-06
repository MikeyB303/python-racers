import subprocess
import time
from die import Die
from python_racer import PythonRacer
from reset_screen import reset_screen

die = Die(6)
players = ['a', 'b']
game = PythonRacer(players, die)
reset_screen()
game.board_visualization()
time.sleep(1)

while game.finished() == False:
  reset_screen()
  game.advance_players()
  game.board_visualization()
  time.sleep(.2)

game.winner()
