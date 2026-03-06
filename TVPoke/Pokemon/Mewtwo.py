from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mewtwo(Psychic):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Water Gun", "WATER", 40),
            Move("Surf", "WATER", 80),
            Move("Splash", "WATER", 0)
        ]
        super().__init__("MewTwo", 80, moves, "./TVPoke/Pokemon/imgs/Mewtwo.png")