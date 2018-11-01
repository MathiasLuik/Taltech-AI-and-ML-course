#1 2 3
#4 5 6
#7 8 9
from utils import (first,Expr, expr,subexpressions
)

from collections import defaultdict
"""
Märgi muutmisel kasuta miinusmärki
-2 2 = 0. saada kontrollida kas vastasmärgiga on 0 

[(-1,2-3),(1,-2,3),...] Konjuktiivse normaalkuju näide.
(-X1vX2v-X3)&(X1v-X2vX3)&(...)

Genereerime tabeli

_________
0 0 0 | 0
0 0 1 | 0
0 1 0 | 0
1 0 0 | 0
_________

Genereeri vastus
_________
1 1 0 | 0
? 1 ? | 0
1 1 0 | 0
_________

Vaja teada kinniste naabrite arvu.

#proovida vastata ühele täpile asukohas 4 vms

"""
gameTable=[[ 1 , 1 , 0 ],
           ["?", 1 ,"?"],
           [ 1 , 1 , 0 ]]
#import binform
def arrayOfHints(gameTable,questionMarkLocations,elementLocation):
    #print()
    print(questionMarkLocations)
    #4
    countRows=len(gameTable)
    countItemsInRow=len(gameTable[0])
    #(one,two,three,four,five,six,seven,eigth,nine)=state    
    if elementLocation<((countRows-1)*countItemsInRow):
        print(countRows)
        
    if elementLocation>3:
        #number=state[numberInState-3]
        print(countRows) 
    if elementLocation%3>0:
        #number=state[numberInState-1]
        print(countRows)
    if elementLocation%3<2:
        #number=state[numberInState+1]
        print(countRows)
    
    return False
def bombLocationsNearQuestionMark(gameTable,questionMarkLocations):
    bombLocationsNearQuestionMark=[] #4
    
    for elementLocation in range(8):
        if arrayOfHints(gameTable,questionMarkLocations,elementLocation):
            bombLocationsNearQuestionMark.append(elementLocation)
        #print(questionMarkLocations)
    i=0
    for row in gameTable:
        for itemInRow in row:
            i+=1
            if itemInRow=="?":
                bombLocationsNearQuestionMark.append(i)
    return bombLocationsNearQuestionMark,i
def findQuestionMarks(gameTable):
    questionMarkPosition=[]
    #countRows=len(gameTable)
    #countItemsInRow=len(gameTable[0])
    i=0
    for row in gameTable:
        for itemInRow in row:
            i+=1
            if itemInRow=="?":
                questionMarkPosition.append(i)
    return questionMarkPosition,i
def listOfIndexes(n):
    indexList=[]
    for x in range(n):
        indexList.append(x+1)
    return indexList
def cnf_sweeper(m,neighbors):
    #CNF component ühe ruudu kohta kus on number sisse kirjutatud
    #ruudul asukohaga 5 on konnu n arv naabreid.
    #neighbors - naabrite list.
    #m on mitmes ruut.
    print("cnf_sweeper")
    n=len(neighbors)
    cnf=[]
    dnf=[]
    for i in range(2**n):
        #print("{:0{n}b}".format(i,n=n))
        binform = "{:0{n}b}".format(i,n=n)
        ones = 0 # ütleb mitu miini on kokku juures
        clauses=[] 
        for j in range(n):
            if binform[j] == "1":
                ones +=1
                clauses.append(-neighbors[j])
            else:
                clauses.append(neighbors[j])
        if ones !=m:
            cnf.append(tuple(clauses))
            print(binform,ones,clauses)
        elif ones==m:
            dnf.append(tuple(clauses))   
            #print(binform,ones,clauses)
    #print(dnf)
    return cnf #,dnf
def mainBrain(gameTable):
    cnfList=cnf_sweeper(1,[4,5,6,7])
    cnfList=cnf_sweeper(1,[5,6]) 
    #dnfList=cnfList[0]
    #cnfList=dnfANDcnf[1]
    #print(dnfList)
    print(cnfList)
    
    questionMarkLocations=findQuestionMarks(gameTable)[0]
    amountOfVariables=findQuestionMarks(gameTable)[1]
    tableArray=listOfIndexes(amountOfVariables)
    
    print(tableArray)
    
    #print(questionMarkLocations)
    for x in range(len(questionMarkLocations)):#4,6
        print(x)
        #bombLocationsNearQuestionMark(gameTable,questionMarkLocations[x])
            
        

mainBrain(gameTable)