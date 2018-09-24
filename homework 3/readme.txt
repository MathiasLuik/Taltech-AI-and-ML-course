= Heuristiline otsing =

== Sissejuhatus ==

J�tkame eelmise harjutustunni tegevust ja muudame oma otsingu heuristiliseks - see t�hendab, et kasutame mingit meetodit et umbkaudu hinnata, mis tee kiiremini lahenduseni viib.

Meeldetuletuseks, otsing toimub ASCII-art formaadis kaardil. Tuleb leida tee kaardil alguspunktist "s" teemandini "D". Seejuures ei tohi tee l�bida kohti, kus on laava (t�histus "*").

Implementeerime ahne otsingu ja A*-i ning katsetame neid etteantud kaartidel suuruses 300x300 kuni 900x900 (paremkl�ps ja ''Save as'' vms):

* [[Media:ITI0210_caves.zip]]

Erinevate strateegiate k�itumine 300x300 kaardil. Roheline t�histab otsingu l�bitud ala, punane leitud teed.

[[Image:Iti0210_300Breadth.png|thumb|none|100px|laiutiotsing]]
[[Image:Iti0210_300Greedy.png|thumb|none|100px|ahne otsing]]
[[Image:Iti0210_300Astar.png|thumb|none|100px|A*]]

Vabatahtlikus lisa�lesandes anal��sime heuristikute k�itumist.

== Ettevalmistus ==

Siin �lesandes olevad n�ited ja juhised eeldavad, et [[Iti0210lab2|2. n�dala �lesanne]] on juba lahendatud. K�ige mugavam on teha selle lahendusest koopia ja hakata seda t�iendama.

Enne kaardi kasutamist tuleb see failist laadida. Et saada samas formaadis kaart, nagu eelmises �lesandes, v�ib j�rgmist koodi kasutada:

<pre>
with open("cave300x300.txt") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]
</pre>

Loomulikult v�ib teha andmetega soovi korral edasisi teisendusi, kui selline esitus mugav ei tundu.

Lisa ka kood, mis otsib kaardilt �les "D" koordinaadid. Seda on vaja heuristilise v��rtuse arvutamise jaoks.

== Ahne otsing ==

Inspiratsiooni heuristilise otsingu tegemiseks saame j�lle [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit tutorialist]. Samast leiad ka animatsioone ja selgitusi nende algoritmide k�itumise kohta.

Ahne otsingu ja laiutiotsingu peamine erinevus on, et ahne otsing �ritab liikuda eelistatult eesm�rgi suunas. Selleks valitakse alati selline j�rgmine punkt, mis on eesm�rgile k�ige l�hemal. Leitud punktide automaatseks j�rjestamiseks kasutame <code>PriorityQueue</code>-t.

<pre>
from queue import Queue, PriorityQueue
</pre>

Tee uus <code>greedy</code> funktsioon, mis on koopia laiutiotsingust ja millel on lisaks parameeter <code>goal</code> (seda on vaja heuristiku jaoks). Muuda seda j�rgmiselt:

<code>frontier</code> on alati sorteeritud elemendi v��rtuse j�rgi (mitte lisamise j�rjekorras)
<pre>
    frontier = PriorityQueue()
    frontier.put((0, start))
</pre>

Uued ruudud lisatakse koos heuristilise v��rtusega, mis aitab �igesti sorteerida.

<pre>
             priority = h(next, goal)
             frontier.put((priority, next))
</pre>

Kuna j�rjekorra formaat muutus, siis tuleb ka sealt asju teistmoodi v�lja v�tta:

<pre>
        _, current = frontier.get()
</pre>

L�puks on meil vaja ka heuristilist funktsiooni ennast. Kuna meil on tegu ruudustikul nelja ilmakaare suunas liikumisega, siis ''Manhattan distance'' on selleks v�ga sobiv.

<pre>
def h(node, goal):
    # implementeeri ise
</pre>

== A* ==

Ahne otsingu ja A* vahel on ainult �ks erinevus: esimesel juhul leitakse heuristiline v��rtus ''f(n) = h(n)'', teisel juhul ''f(n) = g(n) + h(n)''. See t�hendab, et ka senini l�bitud teepikkus m�ngib j�rgmise punkti valimisel rolli. Sel viisil v�lditakse olukordi, kus konstrueeritud teekond suundub otse eesm�rgi suunas, kuni kohtab takistust ning peab siis tagasi p��rduma.

Tee uus funktsioon <code>astar</code>, mis on ahne otsingu koopia.

K�igepealt on vaja ''g(n)'' v��rtusi meelde j�tta.

<pre>
    cost_so_far = {}
    cost_so_far[start] = 0
</pre>

Heuristilise v��rtuse arvutamisel tuleb senine teekond sisse arvestada. J�rgmisse ruutu liikumise maksumus on alati 1. Lisaks tuleb muuta kohta, kus kontrollitakse, kas <code>next</code> on juba n�htud. Nimelt on v�imalik, et me saabume uuesti samasse kohta l�hemat teed m��da ning meid huvitab eelk�ige see uus, l�hem tee.

<pre>
          new_cost = cost_so_far[current] + 1
          if next not in cost_so_far or new_cost < cost_so_far[next]:
             cost_so_far[next] = new_cost
             priority = new_cost + h(next, goal)    # g(n) + h(n)
             frontier.put((priority, next))
             came_from[next] = current
</pre>

Katseta A*-i ja ahnet otsingut k�ikidel kaartidel. Lisa ajav�tmine ning v�rdle leitud teekonna pikkusi ja funktsiooni t�� aega.

== Lisa�lesanne ==

Implementeeri teine heuristiline funktsioon:

  def h2(node, goal):
      return max(abs(node[0]-goal[0]), abs(node[1]-goal[1]))  # suurim koordinaadi nihe

V�rdle A* ja ahne otsingu k�itumist m�lema heuristikuga k�igil kaartidel.

Seej�rel muuda otsingut nii, et lubataks ''diagonaalis'' liikumisi. Mis m�ju on sellel heuristikute efektiivsusele, eriti A* puhul?

== Optimaalsed tulemused ==

Optimaalsed teepikkused

<pre>
300x300 554
600x600 1247
900x900 1843
</pre>
