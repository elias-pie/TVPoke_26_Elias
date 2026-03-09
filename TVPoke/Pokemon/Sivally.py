from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Sivally(Normal):
    def __init__(self):
        moves = [
            Move("Fire", "FIRE", 120),
            Move("Water", "WATER", 120),
            Move("Grass", "GRASS", 120),
            Move("Electric", "ELECTRIC", 120)
        ]
        super().__init__("Sivally", 320, moves, "./TVPoke/Pokemon/imgs/Sivally.png")