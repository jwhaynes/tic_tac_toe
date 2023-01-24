#tic tac toe gameplay

class Player():
    def __init__(self, order):
        self.order = order
        self.plays = []

class Game():
    def __init__(self):
        self.winner = None
        self.p1 = Player(1)
        self.p2 = Player(2)
    
    solutions = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]

    def check_for_win(self):
        for solution in Game.solutions:
            if solution in self.p1.plays:
                self.winner = self.p1
            elif solution in self.p2.plays:
                self.winner = self.p2
    
    def play_game(self):
        while self.winner == None:
            pass
