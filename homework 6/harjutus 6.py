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
        #return random_player
    def actions(self, state):
        movesList=[]# kõik seisus võimalikud käigud
        for x in state:
            if (x!="O" or x!="*"):
                movesList.append(x)
        print(movesList)    
        #moves=[0,1,2,3,4,5,6,7,8]
        print("BearGame.actions")        
        return movesList                                                            
    def result(self, state, action):
        
        print(action)
        
        state[action]="*"
        # uus seis peale käigu tegemist
        print("BearGame.result")
        return state
    def utility(self, state, side):
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli
        print("BearGame.utility")
    def terminal_test(self, state):
        # siin peaks ära tundma, kas karu on lõksu aetud
        print("BearGame.terminal_test")
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