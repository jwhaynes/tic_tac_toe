#tic tac toe gameplay

# player class holds information on players in a given game, instantiated in the game class
class Player():
    def __init__(self, order):
        self.order = order
        self.plays = []

# game class holds game specific variables and functions for playing and checking game status
class Game():
    def __init__(self):
        self.winner = None
        self.p1 = Player(1)
        self.p2 = Player(2)
        self.play_options = [num for num in range(1,10)]
    
    # solutions is a list of sets of the possible solutions in a game of tic tac toe, used for reference in check for win function
    solutions = [
        {1,2,3},
        {4,5,6},
        {7,8,9},
        {1,4,7},
        {2,5,8},
        {3,6,9},
        {1,5,9},
        {3,5,7}
    ]

    # function is used to check for a winner after a play
    def check_for_win(self):
        # turn plays for each player into a set in order to compare to solution sets
        p1_plays = set(self.p1.plays)
        p2_plays = set(self.p2.plays)
 
        #check both players for a winner
        for solution in Game.solutions:
            # use set.issubseet method to check for solutions
            if solution.issubset(p1_plays):
                self.winner = self.p1
            elif solution.issubset(p2_plays):
                self.winner = self.p2
        
        # determine total plays
        total_plays = len(self.p1.plays) + len(self.p2.plays)
        # if all possible plays are made and no winner, winner is CAT
        if total_plays == 9 and self.winner == None:
            self.winner = 'CAT'

    def make_play(self):
        # determine if p1 turn or p2 turn
        if len(self.p1.plays) == len(self.p2.plays):
            ####### NEED TO CHECK IF PLAY IS AVAIALABLE AND THEN REMOVE IT FROM AVAILABLE PLAYS AFTER SELECTED!!! #########
            p1_play = int(input('Select move p1: '))
            self.p1.plays.append(p1_play)
            self.check_for_win()
        else:
            p2_play = int(input('select move p2: '))
            self.p2.plays.append(p2_play)
            self.check_for_win()
    
    def play_game(self):
        while self.winner == None:
            self.make_play()
            print('Player 1 plays: {plays}'.format(moves=self.p1.plays))
            print('Player 2 plays: {plays}'.format(moves=self.p2.plays))
        print('Winner: {winner}'.format(winner=self.winner))

game = Game()
game.play_game()