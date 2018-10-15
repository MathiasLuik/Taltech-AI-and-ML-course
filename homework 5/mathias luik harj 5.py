import search
import random
import re

#https://courses.cs.ttu.ee/pages/ITI0120lab5

def optSwap(route,i,k):
    assert i >= 0 and i < (len(route) - 1)
    assert k > i and k < len(route)
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k+1:])
    assert len(new_route) == len(route)
    return new_route

def readingFile(fileName):
    dist_matrix=[]
    with open(fileName, 'r') as filehandle:  
        next(filehandle)
        for line in filehandle:
            liners=[]  
            line = line.split()
            liners.extend(line)
            dist_matrix.append(liners)            
    return dist_matrix

class TSP(search.Problem):
    def __init__(self, instance):
        value =int(re.search(r'\d+', instance).group())
        list=[]
        for x in range(value):
            list.append(x)
        self.instance=instance
        self.initial=list        
    def actions(self, state):
        optimizeCount=1000
        pairs = [random.sample(range(len(state)), 2) for x in range(optimizeCount)]      
        return pairs
    def result(self, state, action):    
        action.sort()
        i=action[0]
        j=action[1]
        newState=optSwap(state,i,j)
        return newState
    def cost(self, state):
        routeDistance=0
        stateLength=len(state)
        for x in range(stateLength):
            distance=dist_matrix[state[(1+x)%stateLength]][state[(x)%stateLength]]
            routeDistance+=int(distance)
        return routeDistance
    def value(self, state):
        return 1/(self.cost(state)+1)   

dist_matrix=readingFile("gr48.txt")
p = search.InstrumentedProblem(TSP("gr48.txt")) #pead ülevalt ka vahetama

g = search.hill_climbing(p)
print(g)
print(p.cost(g))