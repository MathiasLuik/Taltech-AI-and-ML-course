

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
        print("I'm in EightPuzzle.actions")
        numberInState=find_location(state)
        print(numberInState) #õide
        # returnib actionite listi
        #return action
        print(state)
        return []
    
    def result(self, state, action):
        print("I'm in EightPuzzle.result")
        # returnib UUE oleku
        print(state)
        return state
    def goal_test(self, state):
        print("I'm in EightPuzzle.goal_test")
        if state==(1,2,3,4,5,6,7,8,9,0) :
            print("wowa, you won")
            return True
         #   return True
        # returnib True kui state on lõppolek
    
        return False
        #return True
    def path_cost(self, c, state1, action, state2):
        print("I'm in EightPuzzle.path_cost")
        return c + 1    # uus cost peale ühe sammu tegemist
    
#4 ülesse

#igale indeksile on defineeritud action
#inistate indeks 3='7'
#action peaks olema kas vasak parem vms, ja siis läheb state. Statest tuleb uus action mis annab uue state jne. 
# algselt saab 0 muuta kas 2,7,5 või 4.
        
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
        #print(state[i])
        if state[i]==0:
            
            return i
        
inistate = (1,2,3,7,0,5,8,4,6)
goal =(1,2,3,4,5,6,7,8,9,0) 
def mainBrain(inistate, goal):
    #location=find_location(inistate)
    #print(location)
    problem = EightPuzzle(inistate, goal)
    #print(problem[inistate])
    print("---")
    goalnode = search.breadth_first_graph_search(problem)
    # sammud (tegevused, käigud) algolekust lõppolekuni
    #print(goalnode.solution())
    # olekud algolekust lõppolekuni
    #print(goalnode.path())

mainBrain(inistate,goal)
