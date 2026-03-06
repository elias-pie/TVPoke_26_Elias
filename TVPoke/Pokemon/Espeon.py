from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Espeon(Psychic):
    def __init__(self):
        moves = [
            Move("Psychic", "PSYCHIC", 90),
            Move("Psybeam", "PSYCHIC", 65),
            Move("Stored Power", "PSYCHIC", 860),
            Move("Future Sight", "PSYCHIC", 120)
        ]
        super().__init__("Espeon", 120, moves, "./TVPoke/Pokemon/imgs/Espeon.png")