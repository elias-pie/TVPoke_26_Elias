from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mew(Psychic):
    def __init__(self):
        moves = [
            Move("Pound", "NORMAL", 40),
            Move("Mega Punch", "NORMAL", 80),
            Move("Body Slam", "NORMAL", 80),
            Move("Psychic", "PSYCHIC", 100)
        ]
        super().__init__("Mew", 180, moves, "./TVPoke/Pokemon/imgs/Mew.png")