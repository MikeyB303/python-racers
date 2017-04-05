import random
class Die:
    def __init__(self, side_count):
        self.side_count = side_count
    def roll(self):
        random.randint(0, self.side_count)

die = Die(6)
result = die.roll()
print(result)
