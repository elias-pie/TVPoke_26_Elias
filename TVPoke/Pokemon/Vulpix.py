from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Vulpix(Fire):
    def __init__(self):
        moves = [
            Move("Quick Attack", "NORMAL", 40),
            Move("Tail Whip", "NORMAL", 40),
            Move("Flamethrower", "FIRE", 80),
            Move("Wil-O-Wisp", "FIRE", 80)
        ]
        super().__init__("Vulpix", 120, moves, "./TVPoke/Pokemon/imgs/Vulpix.png")