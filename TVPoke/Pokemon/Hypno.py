from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Hypno(Psychic):
    def __init__(self):
        moves = [ 
            Move("Confusion", "PSYCHIC", 50),
            Move("Future Sight", "PSYCHIC", 120),
            Move("Pound", "NORMAL", 40 ),
            Move("Psybeam", "PSYCHIC", 65)
        ]
        super().__init__("Hypno", 140, moves, "./TVPoke/Pokemon/imgs/Hypno.png")