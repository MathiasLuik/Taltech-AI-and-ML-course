import search
#alpha beta otsing karu mäng
#sama ruudu peal ei saa mitu sõjameest olla
#otsing isegi ei pruugi parima efektiivsusega
import games

class BearGame(games.Game):                                                     
    def __init__(self):
        # algseis jne initsialiseerimine
        initial=[(0,2)]
        return initial
    def to_move(self, state):
        # otsusta, kuidas karu ja jahimeeste poolt t�histada ja tagasta, kumb pool k�igul on
        return 1
    def actions(self, state):
        # k�ik seisus v�imalikud k�igud
        return 1                                                                        
    def result(self, state, action):
        # uus seis peale k�igu tegemist
        return 1
    def utility(self, state, side):
        # mis on seisu v��rtus antud poole jaoks (ei v�rdu alati
        #   sellega, kelle k�ik antud seisus on)
        # t�idab ka eval() funktsiooni rolli
        return 1
    def terminal_test(self, state):
        return 1
        # siin peaks �ra tundma, kas karu on l�ksu aetud
bg = BearGame()

bg.play_game(games.query_player,
              games.random_player)
#