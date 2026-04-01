from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Magmar(Fire):
    def __init__(self):
        moves = [
            Move("Heat Wave", "FIRE", 1000),
            Move("V- Create-", "FIRE", 1800),
            Move("Sacred Fire", "FIRE", 1000),
            Move("Eruption", "FIRE", 2000)
        ]
        super().__init__("Magmar", 50000, moves, "./TVPoke/Pokemon/imgs/Magmar.png")
