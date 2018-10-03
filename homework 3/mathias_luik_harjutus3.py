# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:52:16 2018

@author: mathias.luik
"""
from queue import Queue, PriorityQueue
import numpy as np
#from Graph import *

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]
lava_map3 = [
    "      **            D  **   s  ",
    "     ***              ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                               ",
]

#print(lava_map3[2][20])

def findingPairQueue(map,start,finish):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        if (current==finish):
            print("You found the diamond")
            break
        for next in neighbors(current):       
            #print(len(map))#15 0-14
            #print(len(map[0]))#31 0-30    
            if ((next not in (came_from)) and makingWallCriterias(map,next) and map[next[0]][next[1]]!="*" ):
                #print(next) #(1, 28)
                #print(map[0][next])
                #print(map[14][30])
                #print(map[0]) #0-14
                #print(map[next[0]][next[1]])
                #print(map[next[1]])
                #print(next[0]) #1
                #print(next[1]) #28
                #print(map[next[0]][1]) #
                #print(map[next[1]])  #problemaatiline                
                #print(map[1])
                #print(map[0][1])
                #print(map[0][30])     
                #print(map[next[0]][next[1]])         
                frontier.put(next)  
                came_from[next] = current          
    #print(len(came_from))
    return came_from

def findingPairPriorityQueue(map,start,finish):
    #frontier = Queue()
    frontier = PriorityQueue()
    #frontier.put(start)
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None ## queue puhul esimene element on mõtetu, teine vajalik. 
    while not frontier.empty():
        _, current = frontier.get()
        if (current==finish):
            print("You found the diamond")
            break
        for next in neighbors(current):       
            #print(len(map))#15 0-14
            #print(len(map[0]))#31 0-30    
            if ((next not in (came_from)) and makingWallCriterias(map,next) and map[next[0]][next[1]]!="*" ):        
                #frontier.put(next)
                priority = h(next, finish)
                frontier.put((priority, next))
                came_from[next] = current          
    #print(len(came_from))
    return came_from

def makingWallCriterias(map,next):
    if (next[0]>= 0 and next[1]>= 0 and len(map)>next[0] and len(map[0])>next[1]):
        return True
    else:
        return False

def findingPairA(map,start,finish):
    #frontier = Queue()
    
    frontier = PriorityQueue()
    #frontier.put(start)
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None ## queue puhul esimene element on mõtetu, teine vajalik. 
    cost_so_far = {}
    cost_so_far[start] = 0
    while not frontier.empty():
        _, current = frontier.get()
        new_cost = cost_so_far[current] + 1
        if (current==finish):
            print("You found the diamond")
            break
        for next in neighbors(current):       
            #print(len(map))#15 0-14
            #print(len(map[0]))#31 0-30    
            
            if ((next not in cost_so_far or new_cost < cost_so_far[next]) and makingWallCriterias(map,next) and map[next[0]][next[1]]!="*" ):        
                #frontier.put(next)
                #priority = h(next, finish)
                cost_so_far[next] = new_cost
                priority = new_cost + h(next, finish)    # g(n) + h(n)
                frontier.put((priority, next))
                came_from[next] = current          
    #print(len(cost_so_far))
    return came_from

def h(next, finish):
    (x1, y1) = finish
    (x2, y2) = next
    #print("olen siin")
    return abs(x1 - x2) + abs(y1 - y2)
     
def neighbors(location):
        (x, y) = location
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        return results
        
def path_reverse(came_from, start, finish, map):  
    #for next in map:
        #print(next)        
    print("I'm now reversing path")
    current = finish
    #print(finish)
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    printingMapTracks(map,start,finish,path)
    return path

def printingMapTracks(map,start,finish,path):
    makingEmptyList=[]
    path.pop(0)
    path.pop(len(path)-1)
    for k in range(0,len(map)):
        for u in range(0,len(map[0])):    
            makingEmptyList.append(map[k][u])  
            calculatingEachEleSpot=len(map[0])*k+u
            if (k,u) in path:
                makingEmptyList[calculatingEachEleSpot]="X"         
        listingRowVariable=makingEmptyList[len(map[0])*k:calculatingEachEleSpot]
        print(*listingRowVariable, sep='')
        
def find_location(map,findCharacter):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (map[x][y])==findCharacter:
                results=(x,y)       
    return results

def readingFile():
    with open("cave300x300") as f:
        map_data = [l.strip() for l in f.readlines() if len(l)>1]
    return map_data

def path_constructor(map):
    readingFile
    start=find_location(map,"s")
    finish=find_location(map,"D")
    
    #came_from_queue=findingPairQueue(map,start,finish)
    #pathQueue=path_reverse(came_from_queue,start,finish,map)
    
    #came_from_priority=findingPairPriorityQueue(map,start,finish)
    #pathPriority=path_reverse(came_from_priority,start,finish,map)
    
    came_from_A=findingPairA(map,start,finish)
    pathAstar=path_reverse(came_from_A,start,finish,map)
    #path
    #print(path)
-path_constructor(readingFile())
#path_constructor(lava_map2)
#path_constructor(lava_map2)
    



class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
