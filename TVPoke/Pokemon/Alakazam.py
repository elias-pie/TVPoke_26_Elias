from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Alakazam(Psychic):
    def __init__(self):
        moves = [
            Move("Psychic", "base_attack", 135),
            Move("Calm Mind", "PSYCHIC", 65),
            Move("Recover", "PSYCHIC", 100),
            Move("Thunder bolt", "PSYCHIC", 120)
        ]
        super().__init__("Alakazam", 100, moves, "./TVPoke/Pokemon/imgs/Alakazam.png")
