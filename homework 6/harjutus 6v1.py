import games
#print[0, 1, 2]
#print["3, 4, 5"]
#print["6, 7, 8"]
def replace_at_index(state, index, value):
    replaceList=list(state)
    replaceList[index]=value
    return tuple(replaceList)    

class BearGame(games.Game):                                                     
    def __init__(self):
        print("BearGame.__init__")
        #print(self)
        # algseis jne initsialiseerimine
        #self.initial=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
        #self.initial=[]
        self.initial=["*",1,2,"*",4,"*",6,7,"x"]
    def to_move(self, state):
        
        print(state)
        
        # otsusta, kuidas karu ja jahimeeste poolt tähistada ja tagasta, kumb pool käigul on
        print("BearGame.to_move")
        return state
    def actions(self, state):
        movesList=[]# kõik seisus võimalikud käigud        
        for x in range(len(state)):
            if (state[x]=="*" and x<6 and state[x+3]!="*" and ["*",state[x+3]] not in movesList):  #("*"or".")
                    movesList.append([x,state[x+3]])
            if (state[x]=="*" and x>3 and state[x-3]!="*" and ["*",state[x-3]] not in movesList):
                    movesList.append([x,state[x-3]])  
            if (state[x]=="*" and x%3>0 and state[x-1]!="*" and ["*",state[x-1]] not in movesList):            
                    movesList.append([x,state[x-1]])
            if (state[x]=="*" and x%3<2 and state[x+1]!="*") and ["*",state[x+1]] not in movesList:
                    movesList.append([x,state[x+1]])
        print("BearGame.actions")
        #print(movesList)  
        #1322movesList.sort
        return movesList             
    def result(self, state, action):
        print("BearGame.result")
        print(state)
        newState=state
        newState[action[1]]=state[action[0]]
        newState[action[0]]=action[0]        
        print("Here is newState")
        #newState=replace_at_index(state, index, value)
        print(newState)
        return newState
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
              games.query_player)


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