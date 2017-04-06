class PythonRacer:
    def __init__(self, players, die, length = 30):
        self.die = die
        self.length = length
        self.players = players
        self.player1_position = 0
        self.player2_position = 0
    def finished(self):
        self

    def winner(self):
        self

    def advance_players(self):
        self.player1_position += self.die.roll()
        self.player2_position += self.die.roll()

    def board_visualization(self):
        player1_track = [' '] * self.length
        player2_track = [' '] * self.length
        player1_track[self.player1_position] = self.players[0]
        player2_track[self.player2_position] = self.players[1]
        print('| '.join(player1_track))
        print('| '.join(player2_track))
    