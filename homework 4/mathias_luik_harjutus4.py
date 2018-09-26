

from queue import Queue, PriorityQueue
import numpy as np
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
        print("I'm in actions")
        # returnib actionite listi
        #return action
        print(state)
        return []
    
    def result(self, state, action):
        print("I'm in result")
        # returnib UUE oleku
        print(state)
        return state
    def goal_test(self, state):
        #if state==goal:
        #    print("wowa, you won")
         #   return True
        # returnib True kui state on lõppolek
    
        #return False
        print("I'm here")
        return True
    def path_cost(self, c, state1, action, state2):
        return c + 1    # uus cost peale ühe sammu tegemist
    
def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """
    node = Node(problem.initial) #võtab algoleku
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem): #algselt saab listi actionitest ja siis kõik listi stated proovib läbi. 
            if child.state not in explored and child not in frontier: 
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None    

class Problem(object):

    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError
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
inistate = (1,2,3,7,0,5,8,4,6)
goal =(1,2,3,4,5,6,7,8,9,0) 

a=(1,2,3)
hash(a)
#a[1] on 2
problem = EightPuzzle(inistate, goal)
goalnode = search.breadth_first_graph_search(problem)
# sammud (tegevused, käigud) algolekust lõppolekuni
print(goalnode.solution())
# olekud algolekust lõppolekuni
print(goalnode.path())
