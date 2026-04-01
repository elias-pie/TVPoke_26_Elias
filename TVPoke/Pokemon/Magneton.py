from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Magneton(Electric):
    def __init__(self):
        moves = [
            Move("SonicBoom", "NORMAL", 50),
            Move("Slash", "NORMAL", 80),
            Move("Thunder Shock", "Electric", 50),
            Move("Thunder", "Electric", 120)
        ]  
        super().__init__("Magneton", 110000, moves, "./TVPoke/Pokemon/imgs/Magneton.png")