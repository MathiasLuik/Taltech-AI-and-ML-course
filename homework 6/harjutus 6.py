import games

class BearGame(games.Game):                                                     
    def __init__(self):
        print("BearGame.__init__")
        #print(self)
        # algseis jne initsialiseerimine
        self.initial=[0,1,2,3,4,5,6,7,8]
        
    def to_move(self, state):
        #print(state)
        
        # otsusta, kuidas karu ja jahimeeste poolt tähistada ja tagasta, kumb pool käigul on
        print("BearGame.to_move")
        return state
    def actions(self, state):
        movesList=state# kõik seisus võimalikud käigud
        for x in movesList:
            if (x=="X" or x=="O"):
                movesList.remove(x)
        
          
        #moves=[0,1,2,3,4,5,6,7,8]
        print("BearGame.actions")
        print(movesList)  
        return movesList             
    def result(self, state, action):
        """
        if (state.count("X")%2==0):
            print("XX")
            state[action]="X"
        elif (state.count("O")%2==1):
            print("OO")
            state[action]="O"
        else:
            print("oh something is wrong")
        """
        print(action)
        state[action]="X"
        # uus seis peale käigu tegemist
        print("BearGame.result")
        return state
    def utility(self, state, side):
        print("BearGame.utility")
        print(side)
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli
        print("BearGame.utility")
    def terminal_test(self, state):
    
        # siin peaks ära tundma, kas karu on lõksu aetud
        #print("BearGame.terminal_test")
        #print(state)
        print("")
bg = BearGame()

bg.play_game(games.query_player,
              games.random_player)


"""
if self.random_player:
            print("Computer Turn")
            global count
            depth, alpha, beta, isMax = 9-count, -10, 10, True
            value, place = self.alphaBeta(gameBoard, depth, alpha, beta, isMax)
            print("Computer plays at:", place+1)
        else:
            print("Your Turn...")
            place = int(input("Enter a number from 1 to 9: ")) - 1
            while self.isInvalid(gameBoard, place):
                place = int(input("Enter again:")) - 1
		# Mark the symbol at the calculated or user obtained place.
        gameBoard[place] = self.symbol
"""