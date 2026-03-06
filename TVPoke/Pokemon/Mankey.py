from TVPoke.BaseClasses.PokeTypes import Fighting
from TVPoke.BaseClasses.Move import Move

class Mankey(Fighting):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Low Sweep", "FIGHTING", 65),
            Move("Facade", "NORMAL", 75),
            Move("Close Combat", "FIGHTING", 120)
        ]
        super().__init__("Mankey", 40, moves, "./TVPoke/Pokemon/imgs/Mankey.png")
