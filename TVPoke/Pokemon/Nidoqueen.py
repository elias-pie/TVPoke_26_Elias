from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Nidoqueen(Poison):
    def __init__(self):
        moves = [
            Move("Poisen point", "POISEN", 40),
            Move("Sludge wave", "POISON", 40),
            Move("Body slam", "NORMAL", 80),
            Move("Rock slide", "NORMAL", 0)
        ]
        super().__init__("Nidoqueen", 80, moves, "./TVPoke/Pokemon/imgs/Nidoqueen.png")
