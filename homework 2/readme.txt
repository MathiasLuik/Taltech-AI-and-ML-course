= Esimene katsetus otsinguga =

== Sissejuhatus ==

Antud on kaks kaarti. Kaardi formaat on ASCII-art - ebakonventsionaalne, aga harjutus�lesandeks k�lbab k�ll. Tuleb leida tee kaardil alguspunktist "s" teemandini "D". Seejuures ei tohi tee l�bida kohti, kus on laava (t�histus "*"). Liikuda tohib ainult neljas suunas: �les, alla, vasakule ja paremale (mitte diagonaalis).

Kaart 1:
<pre>
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
</pre>

Kaart 2:
<pre>
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
</pre>

Seda kaarti v�ib vaadata kui ruudustikku, kus iga ruutu t�histab tema ''x'' ja ''y'' koordinaat. Tee leidmiseks kasutame laiutiotsingut (''breadth first search, BFS''). Laiutiotsingu t��p�him�tte animatsioone vaata [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit lehelt]. Sel viisil otsides laava v�ltimine on tegelikult lihtne - tuleb lihtsalt laavaga ruute k�sitleda, nagu l�bimatut seina. Kui algoritm on tee leidnud, siis uurime ka, kuidas tema leitud tulemust t�lgendada ja visualiseerida.

== Ettevalmistus ==

Enne, kui otsingut saab alustada, tuleb kindlaks teha, kus alguspunkt on. Seega otsusta, mida t�histad ''x'' ja ''y'' koordinaatidena (�ks peaks olema read, teine veerud) ning leia "s"-i koordinaadid. Samuti tee kindlaks kaardi suurus ''x'' ja ''y'' suunas. Otsingu implementeerimisel tuleb paratamatult kontrollida, kas mingi koordinaadipaar on kaardil v�i sellest v�ljas.

== Laiutiotsing ==

Kasutame koodit�kki [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit].

<pre>
frontier = Queue()
frontier.put(start)
came_from = {}
came_from[start] = None

while not frontier.empty():
   current = frontier.get()
   for next in graph.neighbors(current):
      if next not in came_from:
         frontier.put(next)
         came_from[next] = current
</pre>

Antud kood alustab otsimist <code>start</code> punktist ning leiab tegelikult teed k�ikidesse punktidesse graafil <code>graph</code>. Seejuures saab leitud teid rekonstrueerida selle alusel, et kui <code>came_from[A] == B</code> siis tee punktist ''A'' alguspunkti l�heb l�bi ''B'' - see t�hendab, et tee tuleb rekonstrueerida tagurpidi sihtpunktist alguspunkti.

Kuna meie �lesanne on pisut erinev, siis peame koodi pisut kohandama. Lisaks realiseerime selle funktsioonina, nii et oleks mugav erinevaid kaarte ette anda.

<pre>
from queue import Queue

def minu_otsing(kaart):
    # leia start, n�iteks tuple kujul (x, y)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        # meid ei huvita k�ik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult j�tame teemandi koordinaadid meelde)

        for next in graph.neighbors(current):  # see osa tuleb suht palju �mber teha.
                                               # tuleb leida sobivad naaberruudud kaardilt
                                               # nagu ta meile ette on antud (�lal, all,
                                               # paremal ja vasakul olev ruut)
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current


    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    return path
</pre>

== Visualiseerimine ==

Mittekohustuslik, aga v�ga kasulik lisa�lesanne:

Kirjuta kood, mis leitud teekonna v�ljastab sellisel ASCII-art kujul (kujutatud tee on suvaline n�ide):

<pre>
      **               **      
     ***     D....    ***      
     ***         .             
                 .    *****    
           ****  .   ********  
           ***   .      *******
 **              .       ******
*****            .****     *** 
*****            . **          
***              .             
              ** .       ******
**            ***.      *******
***             ..       ***** 
                .              
                s              
</pre>