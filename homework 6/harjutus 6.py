import games
#print[0, 1, 2]
#print["3, 4, 5"]
#print["6, 7, 8"]
#emptyMap=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
emptyMap=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
def checkIfSamePlayer(playerTurn):
    if playerTurn=='*':
        return '*'
    else:
        return 'x'
def checkIfOpponent(playerTurn):
    if playerTurn!='x':
        return 'x'
    else:
        return '*'
def checkMoves(state,playerSymbol,enemySymbol):
    movesList=[]# kõik seisus võimalikud käigud        
    for x in range(len(state)):
        if ((state[x]==playerSymbol) and x<6 and state[x+3]!=playerSymbol and state[x+3]!=enemySymbol and [playerSymbol,state[x+3]] not in movesList and [enemySymbol,state[x+3]] not in movesList):  #("*"or".")
                movesList.append([emptyMap[x],emptyMap[x+3]])
        if ((state[x]==playerSymbol) and x>2 and state[x-3]!=playerSymbol and state[x-3]!=enemySymbol and [playerSymbol,state[x-3]] not in movesList and [enemySymbol,state[x-3]] not in movesList):
                movesList.append([emptyMap[x],emptyMap[x-3]])  
        if ((state[x]==playerSymbol) and x%3>0 and state[x-1]!=playerSymbol and state[x-1]!=enemySymbol and [playerSymbol,state[x-1]] not in movesList and [enemySymbol,state[x-1]] not in movesList):            
                movesList.append([emptyMap[x],emptyMap[x-1]])
        if ((state[x]==playerSymbol)  and x%3<2 and state[x+1]!=playerSymbol and state[x+1]!=enemySymbol and [playerSymbol,state[x+1]] not in movesList and [enemySymbol,state[x+1]] not in movesList):
                movesList.append([emptyMap[x],emptyMap[x+1]])
    return movesList
"""
def checkMoves(state,playerSymbol,enemySymbol):
    movesList=[]# kõik seisus võimalikud käigud        
    for x in range(len(state)):
        if (state[x]==playerSymbol and x<6 and state[x+3]!=playerSymbol and state[x+3]!=enemySymbol and [playerSymbol,state[x+3]] not in movesList):  #("*"or".")
                movesList.append([x,state[x+3]])
        if (state[x]==playerSymbol and x>2 and state[x-3]!=playerSymbol and state[x-3]!=enemySymbol and [playerSymbol,state[x-3]] not in movesList):
                movesList.append([x,state[x-3]])  
        if (state[x]==playerSymbol and x%3>0 and state[x-1]!=playerSymbol and state[x-1]!=enemySymbol and [playerSymbol,state[x-1]] not in movesList):            
                movesList.append([x,state[x-1]])
        if (state[x]==playerSymbol and x%3<2 and state[x+1]!=playerSymbol) and state[x+1]!=enemySymbol and [playerSymbol,state[x+1]] not in movesList:
                movesList.append([x,state[x+1]])
    return movesList

def allMoves(state,playerSymbol,enemySymbol):
    movesList=[]# kõik seisus võimalikud käigud        
    for x in range(len(state)):
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x<6 and state[x+3]!=playerSymbol and state[x+3]!=enemySymbol and [playerSymbol,state[x+3]] not in movesList and [enemySymbol,state[x+3]] not in movesList):  #("*"or".")
                movesList.append([x,state[x+3]])
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x>3 and state[x-3]!=playerSymbol and state[x-3]!=enemySymbol and [playerSymbol,state[x-3]] not in movesList and [enemySymbol,state[x-3]] not in movesList):
                movesList.append([x,state[x-3]])  
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x%3>0 and state[x-1]!=playerSymbol and state[x-1]!=enemySymbol and [playerSymbol,state[x-1]] not in movesList and [enemySymbol,state[x-1]] not in movesList):            
                movesList.append([x,state[x-1]])
        if ((state[x]==playerSymbol or state[x]==enemySymbol)  and x%3<2 and state[x+1]!=playerSymbol and state[x+1]!=enemySymbol and [playerSymbol,state[x+1]] not in movesList and [enemySymbol,state[x+1]] not in movesList):
                movesList.append([x,state[x+1]])
    return movesList
"""
def allMoves(state,playerSymbol,enemySymbol):
    movesList=[]# kõik seisus võimalikud käigud        
    for x in range(len(state)):
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x<6 and state[x+3]!=playerSymbol and state[x+3]!=enemySymbol and [playerSymbol,state[x+3]] not in movesList and [enemySymbol,state[x+3]] not in movesList):  #("*"or".")
                movesList.append([x,state[x+3]])
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x>2 and state[x-3]!=playerSymbol and state[x-3]!=enemySymbol and [playerSymbol,state[x-3]] not in movesList and [enemySymbol,state[x-3]] not in movesList):
                movesList.append([x,state[x-3]])  
        if ((state[x]==playerSymbol or state[x]==enemySymbol) and x%3>0 and state[x-1]!=playerSymbol and state[x-1]!=enemySymbol and [playerSymbol,state[x-1]] not in movesList and [enemySymbol,state[x-1]] not in movesList):            
                movesList.append([x,state[x-1]])
        if ((state[x]==playerSymbol or state[x]==enemySymbol)  and x%3<2 and state[x+1]!=playerSymbol and state[x+1]!=enemySymbol and [playerSymbol,state[x+1]] not in movesList and [enemySymbol,state[x+1]] not in movesList):
                movesList.append([x,state[x+1]])
    return movesList


class BearGame(games.Game):                                                     
    def __init__(self):
        print("BearGame.__init__")
        #print(self)
        # algseis jne initsialiseerimine
        #self.initial=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
        #self.initial=[]
        #self.initial=[0,1,2,"*","*","*",6,7,"x"] #* on ründaja ja x on kaitsja ehk karu
        #
        #self.initial=[0,1,2,3,"*","*","*",7,"x"]
        #self.initial=["A1","A2","A3","*","*","*","C1","C2","x"]
        self.initial=['A1','A2','A3','B1','*','*','*','C2','x']
        #self.startingPlayer="*"
        self.toho="oo"
        #self.to_move=["x"]
        #self.to_move='x'
    def to_move(self, state):
        #print(print(players[0].__name_
        # otsusta, kuidas karu ja jahimeeste poolt tähistada ja tagasta, kumb pool käigul on
        print("BearGame.to_move")
        print(state)
        self.side='*'
        #self.side="karu"
        #return 'x'
    def actions(self, state, playerTurn):

        """
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
        """
        #print(self)
        #movesList=checkMoves(state,"*","x")
        
        #movesList=checkMoves(state,"*","x")
        #print(checkIfSamePlayer(playerTurn))
        #print(checkIfOpponent(playerTurn))
        movesList=checkMoves(state,checkIfSamePlayer(playerTurn),checkIfOpponent(playerTurn))
        print("BearGame.actions")
        #print(playerTurn)
        #print(state)
        #print(movesList)
        #print(movesList)  
        #1322movesList.sort
        return movesList             
    def result(self, state, action):
        #print(move)
        #print("BearGame.result")
        #print(state)
        #print(action) #['B2', 'C2']#['A1', 'B1']['B3', 'A3']
        newState=state
        #print(action[0])   #'B2'
        #print(action[1])  #'C2'
        #print(state[action[0]])
        #print(newState[action[0]])
        #print[action[1]]
        #print(state)
        """
        for x in range(len(state)):
            #print(state[x]) #A1
            if state[x]==action[1]:
                print("vahetame edasi")
                print(x)
                print(state[x])
               
                newState[x]=state[x]
            if state[x]==action[0]:
                print("vahetame tagasi")
                print(x)
                print(state[x])
                newState[x]=action[0]
        """
        
        movingToIndex=emptyMap.index(action[1])
        movingFromindex=emptyMap.index(action[0])
        #print(emptyMap.index(action[0]))
        #print(emptyMap.index(action[1]))
        newState[movingToIndex]= state[movingFromindex]
        newState[movingFromindex]=emptyMap[movingFromindex]
        #newState[action[1]]=state[action[0]]
        
        #newState[action[0]]=action[0]        
        print("NewState:")
        #print(state)
        #print(action)
        #newState=replace_at_index(state, index, value)
        print(newState)
        return newState
    def utility(self, state, playerTurn):
        print("BearGame.utility")
        #print(side)
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli
        #print("BearGame.utility")
        #return state.utility if side == 'x' else -state.utility
        if games.Game.terminal_test(self,state, playerTurn):
            return 1
        else:
            return 0
        #return side
    def terminal_test(self, state, playerTurn):
    
        # siin peaks ära tundma, kas karu on lõksu aetud
        print("BearGame.terminal_test")
        #print(state)
        #print(actions(state))
        #if (game.actions(state)==[]):
          #  return False
        movesList=checkMoves(state,'x','*')
        #movesList=checkMoves(state,"x","*")
        if movesList==[]:
            print("YOU WON, no moves left for bear")
            return True
        else:

            return False
bg = BearGame()

def alphabeta_depth8(game, state):
    return games.alphabeta_cutoff_search(state, game, d=8)

#bg.play_game(games.random_player,games.query_player)
bg.play_game(games.query_player, games.query_player)
#bg.play_game(alphabeta_depth8,games.query_player)
"""games.query_player
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