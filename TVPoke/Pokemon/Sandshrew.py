from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Sandshrew(Ground):
    def __init__(self):
        moves = [
            Move("Scratch", "NORMAL", 40),
            Move("Sand Tomb", "GROUND", 35),
            Move("Fury Swipes", "NORMAL", 18),
            Move("Slash", "NORMAL", 70)
        ]
        super().__init__("Sandshrew", 50, moves, "./TVPoke/Pokemon/imgs/Sandshrew.png")