from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Zapdos(Electric):
    def __init__(self):
        moves = [
            Move("Zap Cannon", "ELECTRIC", 120),
            Move("Discharge", "ELECTRIC", 80),
            Move("Thunder", "ELECTRIC", 110),
            Move("Volt Switch", "ELECTRIC", 70)
        ]
        super().__init__("Zapdos", 290, moves, "./TVPoke/Pokemon/imgs/Zapdos.png")