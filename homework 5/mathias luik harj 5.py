import search
## pmst dikstra idee
#Kaar samuti aimaga
# teha list [0 1 2 3 4  ja erinvad indeksid]
#https://courses.cs.ttu.ee/pages/ITI0120lab5
#def cost äkki negatiivse märgiga -1
#või value oleks vastupidi seletama


#2optSwap(route, i, k) {
 #      1. take route[0] to route[i-1] and add them in order to new_route
  #     2. take route[i] to route[k] and add them in reverse order to new_route
   #    3. take route[k+1] to end and add them in order to new_route
    #   return new_route;
   #}
def readingFile():
    with open("gr17.txt") as f:
        first_line = f.readline()
        map_data = [l.strip() for l in f.readlines() if len(l)>1]
        print(first_line)
    return map_data

class TSP(search.Problem):
    def __init__(self, instance):
        print(readingFile())
        # laadi sisse ülesanne sobival kujul
        
        # genereeri algolek (võib olla list linnade indeksitest)
            
    def actions(self, state):
        # siin genereerime võimalikud lahti ühendatavate graafi kaarte paarid 2-Opt jaoks
        #siit actionsitest genereeri kohe 16x16 lahendit. 
        return state
    def result(self, state, action):
        # siin tekitame uue oleku, kus mingid kaared lahti ühendatakse ja teistpidi kokku ühendatakse, kasutades ülalolevat pseudokoodi.
        # action on üks i, j paar.
        return state
    def cost(self, state):
        # arvuta (või leia muul viisil) praeguse marsruudi kogupikkus. Ära unusta, et marsruut on suletud.
        return 1
    def value(self, state):
        # kuna valmis otsingufunktsioonid arvavad, et mida suurem väärtus, seda parem, siis meie minimeerimisülesande TSP
        # lahendamiseks tuleb teepikkusest pöördväärtus võtta.
        return 1/(self.cost(state)+1)
        
print(readingFile())
    #problem = TSP(inistate, goal)   
#p = search.InstrumentedProblem(TSP("gr48"))
#g = search.hill_climbing(p)
#print(g.state)
#print(p.cost(g.state))

# kas see tähendab, et 17 listi.
#kujul [(0,1,2,3,4,5,6,7),(2,3,4,5,6,1,7,0),(4,3,))]
#kujul [(15,320,212,133,514,615,6,7),(320,212,133,53,66,171,73,303),(4,3,))]
#hoia 
#listide listi, kahemõõtmeline massiiv, 