from TVPoke.BaseClasses.PokeTypes import Ghost
from TVPoke.BaseClasses.Move import Move
from random import randint

class Gengar(Ghost):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Gengar", 274, moves, "./TVPoke/Pokemon/imgs/Gengar.png")