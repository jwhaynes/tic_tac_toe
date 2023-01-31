#tic tac toe gameplay

# player class holds information on players in a given game, instantiated in the game class
class Player():
    def __init__(self, order):
        self.order = order
        self.plays = []

    def __repr__(self) -> str:
        return 'Player {}'.format(self.order)

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
    
    
    def play_process(self,player):
        play = None
        while play not in self.play_options:
            print('Please make a valid choice from the following: {choices}'.format(choices = self.play_options))
            play = int(input('Select move: '))
        player.plays.append(play)
        self.play_options.remove(play)
        self.check_for_win()

    def make_play(self):
        # determine if p1 turn or p2 turn
        if len(self.p1.plays) == len(self.p2.plays):
            print('Player 1 turn!')
            self.play_process(self.p1)
        else:
            print('Player 2 turn!')
            self.play_process(self.p2)
            


    def play_game(self):
        while self.winner == None:
            self.make_play()
            print('Player 1 plays: {plays}'.format(plays=self.p1.plays))
            print('Player 2 plays: {plays}'.format(plays=self.p2.plays))
        print('Winner: {winner}'.format(winner=self.winner))

game = Game()
game.play_game()