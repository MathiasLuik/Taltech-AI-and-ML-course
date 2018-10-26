import games

emptyMap=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
def findOpponentSymbol(playerTurn):
    if playerTurn=='*':
        return 'x'
    elif playerTurn=='*':
        return '*'
    else:
        return 'Something fucked'
def checkMoves(state,playerTurn):
    movesList=[]# kõik seisus võimalikud käigud
    opponentSymbol=findOpponentSymbol(playerTurn)   
    for x in range(len(state)):
        if ((state[x]==playerTurn) and x<6 and state[x+3]!=playerTurn and state[x+3]!=opponentSymbol and [playerTurn,state[x+3]] not in movesList and [opponentSymbol,state[x+3]] not in movesList):  #("*"or".")
                movesList.append([emptyMap[x],emptyMap[x+3]])
        if ((state[x]==playerTurn) and x>2 and state[x-3]!=playerTurn and state[x-3]!=opponentSymbol and [playerTurn,state[x-3]] not in movesList and [opponentSymbol,state[x-3]] not in movesList):
                movesList.append([emptyMap[x],emptyMap[x-3]])  
        if ((state[x]==playerTurn) and x%3>0 and state[x-1]!=playerTurn and state[x-1]!=opponentSymbol and [playerTurn,state[x-1]] not in movesList and [opponentSymbol,state[x-1]] not in movesList):            
                movesList.append([emptyMap[x],emptyMap[x-1]])
        if ((state[x]==playerTurn)  and x%3<2 and state[x+1]!=playerTurn and state[x+1]!=opponentSymbol and [playerTurn,state[x+1]] not in movesList and [opponentSymbol,state[x+1]] not in movesList):
                movesList.append([emptyMap[x],emptyMap[x+1]])
    return movesList

class BearGame(games.Game):                                                     
    def __init__(self):
        print("BearGame.__init__")
        #print(self)
        # algseis jne initsialiseerimine
        #self.initial=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
        #self.initial=[]
        #self.initial=[0,1,2,"*","*","*",6,7,"x"] #* on ründaja ja x on kaitsja ehk karu
        #self.initial=[0,1,2,3,"*","*","*",7,"x"]
        #self.initial=["A1","A2","A3","*","*","*","C1","C2","x"]
        #self.emptyMap=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        self.initial=['A1','A2','A3','*','*','*','C1','x','C3']
        #self.startingPlayer="*"
        self.toho="oo"
        #self.to_move=["x"]
        #self.to_move='x'
    def to_move(self, state):
        #print(print(players[0].__name_
        # otsusta, kuidas karu ja jahimeeste poolt tähistada ja tagasta, kumb pool käigul on
        print("BearGame.to_move")
        #print(state)
        #self.side='*'
        #self.side="karu"
        #return '*'
    def actions(self, state, playerTurn):
        movesList=checkMoves(state,playerTurn)
        print("BearGame.actions")
        print(state)
        print(movesList)
        return movesList             
    def result(self, state, action):
        #print(move)
        print("BearGame.result")
        #print(state)
        #print(action) #['B2', 'C2']#['A1', 'B1']['B3', 'A3']['B2', 'C2']['C3', 'C2']['C2', 'C1']
        newState=state
        #print(action)
        movingToIndex=emptyMap.index(action[1])
        movingFromindex=emptyMap.index(action[0])
        newState[movingToIndex]= state[movingFromindex]
        newState[movingFromindex]=emptyMap[movingFromindex]
        #print(newState)
        return newState
    def utility(self, state, playerTurn):
        print("BearGame.utility")
        #print(state)
        #print(playerTurn)
        #print(side)
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli
        #print("BearGame.utility")
        #return state.utility if side == 'x' else -state.utility
        if self.terminal_test(state, '*'):
            return 1
        else:
            return 0
        #return side
    def terminal_test(self, state, playerTurn):
        
        # siin peaks ära tundma, kas karu on lõksu aetud
        print("BearGame.terminal_test")
        #print(state)
        #print(playerTurn)
        movesList=checkMoves(state,findOpponentSymbol(playerTurn))
        #print(movesList)
        #movesList=checkMoves(state,"x","*")
        if movesList==[]:
            print("YOU WON, no moves left for bear")
            return True
        else:

            return False
bg = BearGame()

def alphabeta_depth8(game, state, playerTurn):
    return games.alphabeta_cutoff_search(state, playerTurn, game, d=8)

#bg.play_game(games.random_player,games.query_player)
#bg.play_game(games.query_player, games.query_player)
bg.play_game(alphabeta_depth8,games.query_player)
