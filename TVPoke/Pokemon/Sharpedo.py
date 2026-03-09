from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Sharpedo(Water):
    def __init__(self):
        moves = [
            Move("Aqua Jet", "WATER", 40),
            Move("Liquidation", "WATER", 85),
            Move("Hyper Beam", "NORMAL", 150),
            Move("Skull Bash", "NORMAL", 130)
        ]
        super().__init__("Sharpedo", 70, moves, "./TVPoke/Pokemon/imgs/Sharpedo.png")