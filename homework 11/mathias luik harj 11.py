N="N"
L="L"
H="H"

EMF_EMF=[[0.6,0.01,0.01],[0.2,0.8,0.09],[0.2,0.19,0.9]]
NHL_EMF=[[0.1,0.3,0.8],[0.5,0.4,0.19],[0.4,0.3,0.01]]

#textingActivity=[L,N,N,L,H,N,N,N,N,N,N,H]
#textingActivity=[N,H,L,L,L,N,L,N,L,N,N,L]
textingActivity=[H,L,H,N,N,L,H,N,L,L,L,N]

def calculatingTransition(state,depth,whichArray):
    transitionArray=[]
    #E=EMF_EMF[0][0]*state[0]+EMF_EMF[0][1]*state[1]+EMF_EMF[0][2]*state[2]
    #M=EMF_EMF[1][0]*state[0]+EMF_EMF[1][1]*state[1]+EMF_EMF[1][2]*state[2]
    #F=EMF_EMF[2][0]*state[0]+EMF_EMF[2][1]*state[1]+EMF_EMF[2][2]*state[2]
    for i in range(len(state)):
        variable=EMF_EMF[i][0]*state[0]+EMF_EMF[i][1]*state[1]+EMF_EMF[i][2]*state[2]
        transitionArray.append(variable)
    return transitionArray

def phaseCalcuation(state,whichArray,transitionValue):
    array=[]
    for i in range(len(state)):
        value=NHL_EMF[whichArray][i]*transitionValue[i]
        array.append(value)
    return array

def normalizingToNewState(phaseValue):
    valueSum=sum(phaseValue)
    newStateArray=[]
    for i in phaseValue:
        stateValue=i/valueSum
        stateValue=round(stateValue,2)
        newStateArray.append(stateValue)
    return newStateArray

def arraySentiment(depth):
    getChatActivity=textingActivity[depth]
    if getChatActivity=='N':
        return 0
    elif getChatActivity=='L':
        return 1
    elif getChatActivity=='H':
        return 2
    else:
        print("something wrong in arraySentiment")
    print(getChatActivity)
    
def train(state,depth):
    if depth==(len(textingActivity)-1):
        print("You found last state: ")
        print(state)
        return state
    if depth<len(textingActivity):
        whichArrayForPhase=arraySentiment(depth)
        transitionValue=calculatingTransition(state,depth,whichArrayForPhase)
        #print(transitionValue)
        phase=phaseCalcuation(state,whichArrayForPhase,transitionValue)
        #print(phase)
        newState=normalizingToNewState(phase)
        #print(newState)
        depth+=1
        train(newState,depth)
    
def brain():
    x=1/3
    state=[x,x,x]
    print("Here is starting state")
    print(state)
    startCalculating=train(state,depth=0)
    
if __name__ == "__main__":
    brain()