import subprocess

def reset_screen():
  clear_screen()
  move_to_home()
# Clears the content on the screen. Ah, a fresh canvas.
def clear_screen():
  print(chr(27) + "[2J")
# Moves the insert point in the terminal back to the upper left.
def move_to_home():
  print(chr(27) + "[H")
