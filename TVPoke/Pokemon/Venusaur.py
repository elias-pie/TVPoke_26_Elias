from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class Venusaur(Grass):
    def __init__(self):
        moves = [
            Move("Vine Whip", "GRASS", 45),
            Move("Razor Leaf", "GRASS", 55),
            Move("Leech Seed", "GRASS", 0),
            Move("Solar Beam", "GRASS", 120)
        ]
        super().__init__("Venusaur", 80, moves, "./TVPoke/Pokemon/imgs/Venusaur.png")