= Heuristiline otsing =

== Sissejuhatus ==

Jätkame eelmise harjutustunni tegevust ja muudame oma otsingu heuristiliseks - see tähendab, et kasutame mingit meetodit et umbkaudu hinnata, mis tee kiiremini lahenduseni viib.

Meeldetuletuseks, otsing toimub ASCII-art formaadis kaardil. Tuleb leida tee kaardil alguspunktist "s" teemandini "D". Seejuures ei tohi tee läbida kohti, kus on laava (tähistus "*").

Implementeerime ahne otsingu ja A*-i ning katsetame neid etteantud kaartidel suuruses 300x300 kuni 900x900 (paremklõps ja ''Save as'' vms):

* [[Media:ITI0210_caves.zip]]

Erinevate strateegiate käitumine 300x300 kaardil. Roheline tähistab otsingu läbitud ala, punane leitud teed.

[[Image:Iti0210_300Breadth.png|thumb|none|100px|laiutiotsing]]
[[Image:Iti0210_300Greedy.png|thumb|none|100px|ahne otsing]]
[[Image:Iti0210_300Astar.png|thumb|none|100px|A*]]

Vabatahtlikus lisaülesandes analüüsime heuristikute käitumist.

== Ettevalmistus ==

Siin ülesandes olevad näited ja juhised eeldavad, et [[Iti0210lab2|2. nädala ülesanne]] on juba lahendatud. Kõige mugavam on teha selle lahendusest koopia ja hakata seda täiendama.

Enne kaardi kasutamist tuleb see failist laadida. Et saada samas formaadis kaart, nagu eelmises ülesandes, võib järgmist koodi kasutada:

<pre>
with open("cave300x300.txt") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]
</pre>

Loomulikult võib teha andmetega soovi korral edasisi teisendusi, kui selline esitus mugav ei tundu.

Lisa ka kood, mis otsib kaardilt üles "D" koordinaadid. Seda on vaja heuristilise väärtuse arvutamise jaoks.

== Ahne otsing ==

Inspiratsiooni heuristilise otsingu tegemiseks saame jälle [https://www.redblobgames.com/pathfinding/a-star/introduction.html siit tutorialist]. Samast leiad ka animatsioone ja selgitusi nende algoritmide käitumise kohta.

Ahne otsingu ja laiutiotsingu peamine erinevus on, et ahne otsing üritab liikuda eelistatult eesmärgi suunas. Selleks valitakse alati selline järgmine punkt, mis on eesmärgile kõige lähemal. Leitud punktide automaatseks järjestamiseks kasutame <code>PriorityQueue</code>-t.

<pre>
from queue import Queue, PriorityQueue
</pre>

Tee uus <code>greedy</code> funktsioon, mis on koopia laiutiotsingust ja millel on lisaks parameeter <code>goal</code> (seda on vaja heuristiku jaoks). Muuda seda järgmiselt:

<code>frontier</code> on alati sorteeritud elemendi väärtuse järgi (mitte lisamise järjekorras)
<pre>
    frontier = PriorityQueue()
    frontier.put((0, start))
</pre>

Uued ruudud lisatakse koos heuristilise väärtusega, mis aitab õigesti sorteerida.

<pre>
             priority = h(next, goal)
             frontier.put((priority, next))
</pre>

Kuna järjekorra formaat muutus, siis tuleb ka sealt asju teistmoodi välja võtta:

<pre>
        _, current = frontier.get()
</pre>

Lõpuks on meil vaja ka heuristilist funktsiooni ennast. Kuna meil on tegu ruudustikul nelja ilmakaare suunas liikumisega, siis ''Manhattan distance'' on selleks väga sobiv.

<pre>
def h(node, goal):
    # implementeeri ise
</pre>

== A* ==

Ahne otsingu ja A* vahel on ainult üks erinevus: esimesel juhul leitakse heuristiline väärtus ''f(n) = h(n)'', teisel juhul ''f(n) = g(n) + h(n)''. See tähendab, et ka senini läbitud teepikkus mängib järgmise punkti valimisel rolli. Sel viisil välditakse olukordi, kus konstrueeritud teekond suundub otse eesmärgi suunas, kuni kohtab takistust ning peab siis tagasi pöörduma.

Tee uus funktsioon <code>astar</code>, mis on ahne otsingu koopia.

Kõigepealt on vaja ''g(n)'' väärtusi meelde jätta.

<pre>
    cost_so_far = {}
    cost_so_far[start] = 0
</pre>

Heuristilise väärtuse arvutamisel tuleb senine teekond sisse arvestada. Järgmisse ruutu liikumise maksumus on alati 1. Lisaks tuleb muuta kohta, kus kontrollitakse, kas <code>next</code> on juba nähtud. Nimelt on võimalik, et me saabume uuesti samasse kohta lühemat teed mööda ning meid huvitab eelkõige see uus, lühem tee.

<pre>
          new_cost = cost_so_far[current] + 1
          if next not in cost_so_far or new_cost < cost_so_far[next]:
             cost_so_far[next] = new_cost
             priority = new_cost + h(next, goal)    # g(n) + h(n)
             frontier.put((priority, next))
             came_from[next] = current
</pre>

Katseta A*-i ja ahnet otsingut kõikidel kaartidel. Lisa ajavõtmine ning võrdle leitud teekonna pikkusi ja funktsiooni töö aega.

== Lisaülesanne ==

Implementeeri teine heuristiline funktsioon:

  def h2(node, goal):
      return max(abs(node[0]-goal[0]), abs(node[1]-goal[1]))  # suurim koordinaadi nihe

Võrdle A* ja ahne otsingu käitumist mõlema heuristikuga kõigil kaartidel.

Seejärel muuda otsingut nii, et lubataks ''diagonaalis'' liikumisi. Mis mõju on sellel heuristikute efektiivsusele, eriti A* puhul?

== Optimaalsed tulemused ==

Optimaalsed teepikkused

<pre>
300x300 554
600x600 1247
900x900 1843
</pre>
