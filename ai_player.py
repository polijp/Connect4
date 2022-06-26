from player import Player
from copy import deepcopy
import sys


# What to do with this file ?
# 1) Change the nama of your AI (line 18)
# 2) Implements alpha-beta and its heuristic
# 3) Do not touch or rename anything else


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """

    def __init__(self):
        super().__init__()
        self.name = "my AI name" #puts here the name of your AI: do not let the default one

    
    def getColumn(self, board):
        return self.alphabeta(board)

    
#You can change de depth of your algorithm (by default: 4)
    def alphabeta(self, board, maxdepth=4):


        def heuristic(board,color):
            """
                Evalutes a board and returns an integer.
                board: the current board of the game
                color: indicates who is Max (either -1 or +1)
            """
            # TODO(student): implement this!
            # Note : the greater the value, the better for Max
            if board.winner == color:
                return 100000 #here is the maximum value of your heuristic
            elif board.winner == -color:
                return -100000 #here is the minimum value of your heuristic
            elif board.isFull():
                #draw game: no winner, no looser
                return 0
            else:
                #here, replace the return 0 by your own code
                return 0



#here you should implement alpha beta
#use deepcopy(board) to copy your board
        def maxvalue(board, alpha, beta, depth):
            #terminal test
            if depth>=maxdepth or board.winner!=None or board.isFull():
                return heuristic(board, self.color)

            #finish it
            pass

        def minvalue(board, alpha, beta, depth):
            #terminal test
            if depth>=maxdepth or board.winner!=None or board.isFull():
                return heuristic(board, self.color)
            
            #finish it
            pass

        #do not touch below
        best_score = -sys.maxsize
        beta = sys.maxsize
        coup = None
        possibleplays = board.getPossibleColumns()
        if len(possibleplays)==0:
            raise Exception("cannot have 0 possible play")
        elif len(possibleplays)==1:
            return possibleplays[0]
        else:
            for action in possibleplays:
                boardcopy = deepcopy(board)
                boardcopy.play(self.color, action)
                v = minvalue(boardcopy, best_score, beta, 1)
                if v>best_score:
                    best_score = v
                    coup = action

            return coup
            
        
            

