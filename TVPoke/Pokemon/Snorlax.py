from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Snorlax(Normal):
    def __init__(self):
        moves = [
            Move("Amnesia", "PSYCHIC", 0),
            Move("Headbutt", "NORMAL", 70),
            Move("Rest", "PSYCHIC", 0),
            Move("Body Slam", "NORMAL", 85)
        ]
        super().__init__("Snorlax", 110, moves, "./TVPoke/Pokemon/imgs/Snorlax.png")