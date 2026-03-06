from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Marill(Water):
    def __init__(self):
        moves = [
            Move("Double Edge", "NORMAL", 120),
            Move("Hydro Vortex", "WATER", 185),
            Move("All Out Pummeling", "FIGHTING", 200),
            Move("Z-Belly Drum", "NORMAL", 0)
        ]
        super().__init__("Marill", 344, moves, "./TVPoke/Pokemon/imgs/Marill.png")