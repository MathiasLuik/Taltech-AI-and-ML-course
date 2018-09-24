# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:52:16 2018

@author: mathias.luik
"""
from queue import Queue
from Graph import *

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

def findingPair(map,start,finish):
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
            if ((next not in (came_from)) and next[0]>= 0 and next[1]>= 0 and len(map)>next[0] and len(map[0])>next[1] and map[next[0]][next[1]]!="*" ):
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
    #print(came_from)
    return came_from
def neighbors(location):
        (x, y) = location
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        return results
def path_reverse(came_from, start, finish):
    #print(came_from)
    print("I'm now reversing path")
    current = finish
    print(finish)
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
        print(current)
    path.reverse()
    #print(path)
    return path
def find_location(map,findCharacter):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (map[x][y])==findCharacter:
                results=(x,y)       
    return results
def path_constructor(map):
    start=find_location(map,"s")
    finish=find_location(map,"D")
    came_from=findingPair(map,start,finish)
    path=path_reverse(came_from,start,finish)
    #path
    #print(path)
path_constructor(lava_map2)
    

