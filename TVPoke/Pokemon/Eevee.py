from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Eevee(Normal):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Quick Attack", "NORMAL", 40),
            Move("Bite", "NORMAL", 60),
            Move("Take Down", "NORMAL", 90)
        ]
        super().__init__("Eevee", 100, moves, "./TVPoke/Pokemon/imgs/Eevee.png")