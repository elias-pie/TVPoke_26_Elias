from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Gyrados(Water):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Water Gun", "WATER", 40),
            Move("Surf", "WATER", 80),
            Move("Splash", "WATER", 0)
        ]
        super().__init__("Gyrados", 80, moves, "./TVPoke/Pokemon/imgs/Gyrados.png")