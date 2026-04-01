from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Porygon(Normal):
    def __init__(self):
        moves = [
            Move("Zap Cannon", "ELECTRIC", 120),
            Move("Giga Impact", "NORMAL", 150),
            Move("Black Hole Eclpise", "DARK", 175),
            Move("Recover", "NORMAL", 0)
        ]
        super().__init__("Porygon", 334, moves, "./TVPoke/Pokemon/imgs/Porygon.png")