from die import Die
from python_racer import PythonRacer

die = Die(6)
game = PythonRacer(die)
print(game.die.roll())
