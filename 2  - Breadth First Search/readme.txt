= Esimene katsetus otsinguga =

== Sissejuhatus ==

Antud on kaks kaarti. Kaardi formaat on ASCII-art - ebakonventsionaalne, aga harjutusülesandeks kõlbab küll. Tuleb leida tee kaardil alguspunktist "s" teemandini "D". Seejuures ei tohi tee läbida kohti, kus on laava (tähistus "*"). Liikuda tohib ainult neljas suunas: üles, alla, vasakule ja paremale (mitte diagonaalis).

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

Seda kaarti võib vaadata kui ruudustikku, kus iga ruutu tähistab tema ''x'' ja ''y'' koordinaat. Tee leidmiseks kasutame laiutiotsingut (''breadth first search, BFS''). Laiutiotsingu tööpõhimõtte animatsioone vaata [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit lehelt]. Sel viisil otsides laava vältimine on tegelikult lihtne - tuleb lihtsalt laavaga ruute käsitleda, nagu läbimatut seina. Kui algoritm on tee leidnud, siis uurime ka, kuidas tema leitud tulemust tõlgendada ja visualiseerida.

== Ettevalmistus ==

Enne, kui otsingut saab alustada, tuleb kindlaks teha, kus alguspunkt on. Seega otsusta, mida tähistad ''x'' ja ''y'' koordinaatidena (üks peaks olema read, teine veerud) ning leia "s"-i koordinaadid. Samuti tee kindlaks kaardi suurus ''x'' ja ''y'' suunas. Otsingu implementeerimisel tuleb paratamatult kontrollida, kas mingi koordinaadipaar on kaardil või sellest väljas.

== Laiutiotsing ==

Kasutame kooditükki [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit].

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

Antud kood alustab otsimist <code>start</code> punktist ning leiab tegelikult teed kõikidesse punktidesse graafil <code>graph</code>. Seejuures saab leitud teid rekonstrueerida selle alusel, et kui <code>came_from[A] == B</code> siis tee punktist ''A'' alguspunkti läheb läbi ''B'' - see tähendab, et tee tuleb rekonstrueerida tagurpidi sihtpunktist alguspunkti.

Kuna meie ülesanne on pisut erinev, siis peame koodi pisut kohandama. Lisaks realiseerime selle funktsioonina, nii et oleks mugav erinevaid kaarte ette anda.

<pre>
from queue import Queue

def minu_otsing(kaart):
    # leia start, näiteks tuple kujul (x, y)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)

        for next in graph.neighbors(current):  # see osa tuleb suht palju ümber teha.
                                               # tuleb leida sobivad naaberruudud kaardilt
                                               # nagu ta meile ette on antud (ülal, all,
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

Mittekohustuslik, aga väga kasulik lisaülesanne:

Kirjuta kood, mis leitud teekonna väljastab sellisel ASCII-art kujul (kujutatud tee on suvaline näide):

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