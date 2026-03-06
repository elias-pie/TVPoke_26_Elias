from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Geodude(Ground):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 1000),
            Move("Punch", "NORMAL", 1000),
            Move("Earthquake", "NORMAL", 50000),
            Move("Crunch", "NORMAL", 1000)
        ]
        super().__init__("Geodude", 1000000, moves, "./TVPoke/Pokemon/imgs/Geodude.png")