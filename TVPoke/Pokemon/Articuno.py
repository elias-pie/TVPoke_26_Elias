from TVPoke.BaseClasses.PokeTypes import Ice
from TVPoke.BaseClasses.Move import Move

class Articuno(Ice):
    def __init__(self):
        moves = [
            Move("Freeze-Dry", "ICE", 60),
            Move("Ice Beam", "ICE", 80),
            Move("Hurricane", "WATER", 80),
            Move("Roost", "FLYING", 0)
        ]
        super().__init__("Articuno", 65, moves, "./TVPoke/Pokemon/imgs/Articuno.png")