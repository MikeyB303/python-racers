import subprocess
import time
from die import Die
from python_racer import PythonRacer
from reset_screen import reset_screen

die = Die(6)
players = ['a', 'b']
game = PythonRacer(players, die)

while True:

  reset_screen()
  game.board_visualization()
  game.advance_players()
  time.sleep(.2)
