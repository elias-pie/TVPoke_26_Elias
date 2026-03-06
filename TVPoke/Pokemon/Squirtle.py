from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Squirtle(Water):
    def __init__(self):
        moves = [
            Move("Water Gun", "WATER", 40),
            Move("Bubble Beam", "WATER", 65),
            Move("Icy Wind", "ICE", 55),
            Move("Liquidation", "WATER", 85)
        ]
        super().__init__("Squirtle", 44, moves, "./TVPoke/Pokemon/imgs/Squirtle.png")