#1 2 3
#4 5 6
#7 8 9
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
#import binform
def cnf_sweeper(m,neighbors):
    #CNF component ühe ruudu kohta kus on number sisse kirjutatud
    #ruudul asukohaga 5 on konnu n arv naabreid.
    #neighbors - naabrite list.
    #m on mitmes ruut.
    
    print("cnf_swwper")
    n=len(neighbors)
    cnf=[]
    for i in range(2**n):
        print("{:0{n}b}".format(i,n=n))
        binform = "{:0{n}b}".format(i,n=n)
        ones = 0
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
        #print(binform)
    return cnf
        
    
# 4, 5, 6, 7 tähendav kordinaati
test=cnf_sweeper(1,[4,5,6,7])    
print(test)
    
    
    
    
    
"""
class EightPuzzle(search.Problem):
    def actions(self, state):
        # returnib actionite listi
        return []
    
    def result(self, state, action):
        # returnib UUE oleku
        return sate
    def goal_test(self, state):
        # returnib True kui state on lõppolek
        return state
    def path_cost(self, c, state1, action, state2):
        return c + 1    # uus cost peale ühe sammu tegemist
"""