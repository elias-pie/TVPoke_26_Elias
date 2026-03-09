from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Lickitung(Normal):
    def __init__(self):
        moves = [
            Move("Power Whip", "GRASS", 120),
            Move("Earthquake", "GROUND", 100),
            Move("Body Slam", "NORMAL", 85),
            Move("Knock Off", "DARK", 65)
        ]
        super().__init__("Lickitung", 90, moves, "./TVPoke/Pokemon/imgs/Lickitung.png")
