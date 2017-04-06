class PythonRacer:
    def __init__(self, players, die, length = 30):
        self.die = die
        self.length = length
        self.players = players
        self.player1_position = 0
        self.player2_position = 0
    def finished(self):
        if self.player1_position == self.length - 1:
            return True
        elif self.player2_position == self.length - 1:
            return True
        else:
            return False

    def winner(self):
        if self.player1_position == self.length - 1 and self.player2_position == self.length - 1:
            print("It's a tie!")
        elif self.player1_position == self.length - 1:
            print('Player 1 is the winner!')
        elif self.player2_position == self.length - 1:
            print('Player 2 is the winner!')
        else:
            print('How did I get here?')


    def advance_players(self):
        self.player1_position += self.die.roll()
        self.player2_position += self.die.roll()
        if self.player1_position >= self.length:
           self.player1_position = self.length - 1
        
        if self.player2_position >= self.length:
           self.player2_position = self.length - 1    


    def board_visualization(self):
        player1_track = [' '] * self.length
        player2_track = [' '] * self.length
        player1_track[self.player1_position] = self.players[0]
        player2_track[self.player2_position] = self.players[1]
        print('| '.join(player1_track))
        print('| '.join(player2_track))
    