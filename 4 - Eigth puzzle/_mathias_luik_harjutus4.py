

#from Graph import *
#Depth-first search
#https://github.com/aimacode/aima-python
# tee sinna samasse zipi oma kataloog. Aima python master
#kui tahta tükke kasutada siis 
# meid huvitav search. problem class. Mis on vajalik lahenduseks
#problem initial on x
#S(x) on action mis annab (a1,s1)(a2,s2)...m
#parim andmetüüp on tuple thistuple = ("apple", "banana", "cherry")
import search

class EightPuzzle(search.Problem):
    def actions(self, state):
        #print("I'm in EightPuzzle.actions")
        numberInState=find_location(state)
        #print(numberInState) #õide
        #ohho=actionList(state,numberInState)
        # returnib actionite listi
        #return action
        #print(state)
        #print(actionList(state,numberInState))
        return actionList(state,numberInState)
    
    def result(self, state, action):
        #print("I'm in EightPuzzle.result")
        #print(action)
        
        #print(EightPuzzle.actions(self,state))
        #print(EightPuzzle.actions)
        
        # returnib UUE oleku
        #print(state)
        return action
    def goal_test(self, state):
        #print(state)
        #print(goal)
        #print("I'm in EightPuzzle.goal_test")
        #print(state)
        if state==goal:
            #print("XXXXXXXXXXXXXXXX")
            print("WOWA, you found solution")
            #exit
            return True
         #   return True
        # returnib True kui state on lõppolek
    
        return False
        #return True
    def path_cost(self, c, state1, action, state2):
        #print("I'm in EightPuzzle.path_cost")
        return c + 1    # uus cost peale ühe sammu tegemist
    
#4 ülesse
def actionList(state,numberInState):
    #print(state)
    
    #numberOfStates=howManyEmptyElementhasMoves(state,numberInState)
    #states=generatingListofTuplesForAction(state,numberInState,numberOfStates)
    #print(states)
    states=generatingListofTuplesForAction(state,numberInState)
    #(x, y) = location
    #results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
    return states

def howManyEmptyElementhasMoves(state,numberInState):
    if (numberInState == 0 or numberInState == 2 or numberInState == 6 or numberInState == 8):
        howManyGeneratedStates=2
    elif (numberInState == 1 or numberInState == 3 or numberInState == 5 or numberInState == 7):
        howManyGeneratedStates=3
    elif (numberInState == 4):
        howManyGeneratedStates=4
    else:
        print("Something is wrong with tuple array")
    #print(howManyGeneratedStates)
    return howManyGeneratedStates
def replace_at_index(state, index, value):
    replaceList=list(state)
    replaceList[index]=value
    return tuple(replaceList)

def generatingListofTuplesForAction(state,numberInState):
    #print("Starts---")
    results=[]
    #(one,two,three,four,five,six,seven,eigth,nine)=state    
    if numberInState<6:
        number=state[numberInState+3]
        movingZero=replace_at_index(state,numberInState+3,0)
        movingNumber=replace_at_index(movingZero,numberInState,number)
        results.append(movingNumber)
    if numberInState>3:
        number=state[numberInState-3]
        movingZero=replace_at_index(state,numberInState-3,0)
        movingNumber=replace_at_index(movingZero,numberInState,number)
        results.append(movingNumber)    
    if numberInState%3>0:
        number=state[numberInState-1]
        movingZero=replace_at_index(state,numberInState-1,0)
        movingNumber=replace_at_index(movingZero,numberInState,number)
        results.append(movingNumber)
    if numberInState%3<2:
        number=state[numberInState+1]
        movingZero=replace_at_index(state,numberInState+1,0)
        movingNumber=replace_at_index(movingZero,numberInState,number)
        results.append(movingNumber)    
    #print(results)
    return results
#igale indeksile on defineeritud action
#inistate indeks 3='7'
#action peaks olema kas vasak parem vms, ja siis läheb state. Statest tuleb uus action mis annab uue state jne. 
# algselt saab 0 muuta kas 2,7,5 või 4.
#print(0%4)     
#1 2 3
#7 0 5
#8 4 6
#osad algoritmid kontrollivad kas tekib tsükkel või mitte. Osad kontrollivad.
#proovida erinevaid strateegijad mitte on parim algo.
#leia esmalt tühja koha indeks. ja tema naabrid. 
# leiad indeks 8-5, indeks 7-4, indeks 6-3 ja 5-2,4-1,3-0 ja saad teada, et moved peavad olema seotud 3ga ülesse ja alla . See on püsti
# kõrvale minnes on -1. Indeks 2-1
def find_location(state):
    i=-1
    for number in state:
        i+=1
        if state[i]==0:
            return i
#inistate = (1,2,3,4,5,6,7,0,8) 
#inistate = (0,2,3,4,5,6,7,1,8)  
inistate = (1,2,3,7,0,5,8,4,6)
#inistate = (0,2,3,7,1,5,8,4,6)            
goal =      (1,2,3,4,5,6,7,8,0) 

def mainBrain(inistate, goal):
    #location=find_location(inistate)
    #print(location)
    problem = EightPuzzle(inistate, goal)
    #print(problem[inistate])
    #print("---")
    #goalnode = search.breadth_first_graph_search(problem)
    goalnode = search.breadth_first_graph_search(problem)
    #goalnode = search.depth_first_graph_search(problem)
    #goalnode = search.iterative_deepening_search(problem)
    # sammud (tegevused, käigud) algolekust lõppolekuni
    print(goalnode.solution())
    print(goalnode.path())
    #print(len(goalnode.path()))
    #print("aa")
    #print(len(goalnode.solution()))
    #print("aa")
    print("----------------------")
    search.compare_searchers([problem], ["Strategy", "firstState"],
                      searchers=[search.breadth_first_graph_search]) #pakun esimene number tähendab mitmes neuroni ringi. 3 tähendab kokku arvutust
    #esimene on self.problem.actions(state)
    #teine on self.problem.result(state, action)
    #kolmas on problem.goal_test(state) 
    #Strateegia nimi ning algolek. 
    # olekud algolekust lõppolekuni
    #print(goalnode.path())

mainBrain(inistate,goal)
