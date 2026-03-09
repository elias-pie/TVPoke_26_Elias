from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Greninja(Water):
    def __init__(self):
        moves = [
            Move("Hydro Pump", "WATER", 110),
            Move("Water Gun", "WATER", 40),
            Move("Surf", "WATER", 80),
            Move("Dark Pulse", "DARK", 80)
        ]
        super().__init__("Greninja", 80, moves, "./TVPoke/Pokemon/imgs/Greninja.png")
