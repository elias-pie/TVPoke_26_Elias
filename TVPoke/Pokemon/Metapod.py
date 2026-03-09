from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Metapod(Poison):
    def __init__(self):
        moves = [
            Move("Harden [does nothing]", "NORMAL", 0),
            Move("String Shot ", "NORMAL", 20),
            Move("Harden [does nothing]", "NORMAL", 0),
            Move("Splash [does nothing]", "NORMAL", 0)
        ]
        super().__init__("Metapod", 40, moves, "./TVPoke/Pokemon/imgs/Metapod.png")
