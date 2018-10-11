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
def readingFile(fileName):
    dist_matrix=[]
    with open(fileName, 'r') as filehandle:  
        numberOfCities=filehandle.readline()
        next(filehandle)
        for line in filehandle:
            liners=[]  
            line = line.split()
            #print(line)
            liners.extend(line)
            dist_matrix.append(liners)
    print(numberOfCities)
    return dist_matrix,numberOfCities

class TSP(search.Problem):
    def __init__(self, instance):
        #(dist_matrix,numberOfCities)=readingFile("gr17.txt")
        list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]# 15st saab nulli         
        self.instance=instance
        self.initial=list

        
    def actions(self, state):
        print(state)
        (dist_matrix,numberOfCities)=readingFile("gr17.txt")
        print(dist_matrix[0][4])
        #siin ta teeb paare. Järestiku ei saa võtta. kui on indeks 4. siis proovib vähemalt 2 või 6te
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




    #problem = TSP(inistate, goal)   
p = search.InstrumentedProblem(TSP("gr17.txt")) #´ta loeb TSP sisse ja selle peale laob searchi problemi
g = search.hill_climbing(p)
#print(g.state)
#print(p.cost(g.state))

# kas see tähendab, et 17 listi.
#kujul [(0,1,2,3,4,5,6,7),(2,3,4,5,6,1,7,0),(4,3,))]
#kujul [(15,320,212,133,514,615,6,7),(320,212,133,53,66,171,73,303),(4,3,))]
#hoia 
#listide listi, kahemõõtmeline massiiv, 