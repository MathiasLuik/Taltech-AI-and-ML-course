#1 2 3
#4 5 6
#7 8 9
from utils import (
    removeall, unique, first, argmax, probability,
    isnumber, issequence, Expr, expr, subexpressions
)

from collections import defaultdict
"""
Märgi muutmisel kasuta miinusmärki
-2 2 = 0. saada kontrollida kas vastasmärgiga on 0 

[(-1,2-3),(1,-2,3),...] Konjuktiivse normaalkuju näide.
(-X1vX2v-X3)&(X1v-X2vX3)&(...)


Näide 
_________

Genereeri vastus
_________
1 1 | 
? 1 | 
1 1 | 
_________
Genereerime tabeli
annab teada, et CNF on 3. mis on vastand, tegelt on -3
kõik ütlevad, et 3ndas on miin ehk cnf = 6. Kui lisan alfa mis on -6. Kui see on ei ole võrdne siis seal vale ehk on miin
Kui alfa on kbs true siis seal pole pommi
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
def eliminate_implications(s):
    """Change implications into equivalent form with only &, |, and ~ as logical operators."""
    s = expr(s)
    if not s.args or is_symbol(s.op):
        return s  # Atoms are unchanged.
    args = list(map(eliminate_implications, s.args))
    a, b = args[0], args[-1]
    if s.op == '==>':
        return b | ~a
    elif s.op == '<==':
        return a | ~b
    elif s.op == '<=>':
        return (a | ~b) & (b | ~a)
    elif s.op == '^':
        assert len(args) == 2  # TODO: relax this restriction
        return (a & ~b) | (~a & b)
    else:
        assert s.op in ('&', '|', '~')
        return Expr(s.op, *args)
def is_symbol(s):
    """A string s is a symbol if it starts with an alphabetic char.
    >>> is_symbol('R2D2')
    True
    """
    return isinstance(s, str) and s[:1].isalpha()

def move_not_inwards(s):
    """Rewrite sentence s by moving negation sign inward.
    >>> move_not_inwards(~(A | B))
    (~A & ~B)
    """
    s = expr(s)
    if s.op == '~':
        def NOT(b):
            return move_not_inwards(~b)
        a = s.args[0]
        if a.op == '~':
            return move_not_inwards(a.args[0])  # ~~A ==> A
        if a.op == '&':
            return associate('|', list(map(NOT, a.args)))
        if a.op == '|':
            return associate('&', list(map(NOT, a.args)))
        return s
    elif is_symbol(s.op) or not s.args:
        return s
    else:
        return Expr(s.op, *list(map(move_not_inwards, s.args)))


def distribute_and_over_or(s):
    """Given a sentence s consisting of conjunctions and disjunctions
    of literals, return an equivalent sentence in CNF.
    >>> distribute_and_over_or((A & B) | C)
    ((A | C) & (B | C))
    """
    s = expr(s)
    if s.op == '|':
        s = associate('|', s.args)
        if s.op != '|':
            return distribute_and_over_or(s)
        if len(s.args) == 0:
            return False
        if len(s.args) == 1:
            return distribute_and_over_or(s.args[0])
        conj = first(arg for arg in s.args if arg.op == '&')
        if not conj:
            return s
        others = [a for a in s.args if a is not conj]
        rest = associate('|', others)
        return associate('&', [distribute_and_over_or(c | rest)
                               for c in conj.args])
    elif s.op == '&':
        return associate('&', list(map(distribute_and_over_or, s.args)))
    else:
        return s
def associate(op, args):
    """Given an associative op, return an expression with the same
    meaning as Expr(op, *args), but flattened -- that is, with nested
    instances of the same op promoted to the top level.
    >>> associate('&', [(A&B),(B|C),(B&C)])
    (A & B & (B | C) & B & C)
    >>> associate('|', [A|(B|(C|(A&B)))])
    (A | B | C | (A & B))
    """
    args = dissociate(op, args)
    if len(args) == 0:
        return _op_identity[op]
    elif len(args) == 1:
        return args[0]
    else:
        return Expr(op, *args)


_op_identity = {'&': True, '|': False, '+': 0, '*': 1}
#import binform
def dissociate(op, args):
    """Given an associative op, return a flattened list result such
    that Expr(op, *result) means the same as Expr(op, *args).
    >>> dissociate('&', [A & B])
    [A, B]
    """
    result = []

    def collect(subargs):
        for arg in subargs:
            if arg.op == op:
                collect(arg.args)
            else:
                result.append(arg)
    collect(args)
    return result
def disjuncts(s):
    """Return a list of the disjuncts in the sentence s.
    >>> disjuncts(A | B)
    [A, B]
    >>> disjuncts(A & B)
    [(A & B)]
    """
    return dissociate('|', [s])
def conjuncts(s):
    """Return a list of the conjuncts in the sentence s.
    >>> conjuncts(A & B)
    [A, B]
    >>> conjuncts(A | B)
    [(A | B)]
    """
    return dissociate('&', [s])
def pl_resolve(ci, cj):
    """Return all clauses that can be obtained by resolving clauses ci and cj."""
    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                dnew = unique(removeall(di, disjuncts(ci)) +
                              removeall(dj, disjuncts(cj)))
                clauses.append(associate('|', dnew))
    return clauses
def to_cnf(s):
    """Convert a propositional logical sentence to conjunctive normal form.
    That is, to the form ((A | ~B | ...) & (B | C | ...) & ...) [p. 253]
    >>> to_cnf('~(B | C)')
    (~B & ~C)
    """
    s = expr(s)
    if isinstance(s, str):
        s = expr(s)
    s = eliminate_implications(s)  # Steps 1, 2 from p. 253
    s = move_not_inwards(s)  # Step 3
    return distribute_and_over_or(s)  # Step 4
def pl_resolution(KB, alpha):
    """Propositional-logic resolution: say if alpha follows from KB. [Figure 7.12]
    >>> pl_resolution(horn_clauses_KB, A)
    True
    """
    clauses = KB.clauses + conjuncts(to_cnf(~alpha))
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)
            if False in resolvents:
                return True
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            return False
        for c in new:
            if c not in clauses:
                clauses.append(c)
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
def resolution_entails(kb, alpha):
    print(kb)
    #if 
    return False
    # kb - teadmusbaas CNF kujul
    # alpha - literaal, mida tahame kontrollida.
def mainBrain(gameTable):
    KB=cnf_sweeper(1,[4,5])
    #KB=cnf_sweeper(1,[6])
    #print(KB)
    #pl_resolution(KB, 8)
    #cnfListOne=cnf_sweeper(1,[4,5]) 
    #cnfListTwo=cnf_sweeper(1,[4,5,6]) 
    #cnfListThree=cnf_sweeper(0,[5,6]) 
    #print(cnfListOne)
    #dnfList=cnfList[0]
    #cnfList=dnfANDcnf[1]
    #print(dnfList)
    #print(cnfList)
    #resolution_entails(cnfList, 6)
    
    questionMarkLocations=findQuestionMarks(gameTable)[0]
    amountOfVariables=findQuestionMarks(gameTable)[1]
    tableArray=listOfIndexes(amountOfVariables)
    #alfa valel kujul, kui kõik maha taanduvad muutub trueks.
    print(tableArray)
    
    #print(questionMarkLocations)
    for x in range(len(questionMarkLocations)):#4,6
        print(x)
        #bombLocationsNearQuestionMark(gameTable,questionMarkLocations[x])
            
        

mainBrain(gameTable)