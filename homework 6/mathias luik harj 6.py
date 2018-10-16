import search
#alpha beta otsing karu mÃ¤ng
#sama ruudu peal ei saa mitu sÃµjameest olla
#otsing isegi ei pruugi parima efektiivsusega
import games

class BearGame(games.Game):                                                     
    def __init__(self):
        # algseis jne initsialiseerimine
        initial=[(0,2)]
        return initial
    def to_move(self, state):
        # otsusta, kuidas karu ja jahimeeste poolt tähistada ja tagasta, kumb pool käigul on
        return 1
    def actions(self, state):
        # kõik seisus võimalikud käigud
        return 1                                                                        
    def result(self, state, action):
        # uus seis peale käigu tegemist
        return 1
    def utility(self, state, side):
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli
        return 1
    def terminal_test(self, state):
        return 1
        # siin peaks ära tundma, kas karu on lõksu aetud
bg = BearGame()

bg.play_game(games.query_player,
              games.random_player)
#