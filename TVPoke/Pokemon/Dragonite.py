from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Dragonite(Fire):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Fire Punch", "FIRE", 80),
            Move("Body Slam", "NORMAL", 80),
            Move("Wing Attack", "FLYING", 120)
        ]
        super().__init__("Dragonite", 120, moves, "./TVPoke/Pokemon/imgs/Dragonite.png")        