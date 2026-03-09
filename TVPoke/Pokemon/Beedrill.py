from TVPoke.BaseClasses.PokeTypes import Bug
from TVPoke.BaseClasses.Move import Move

class Beedrill(Bug):
    def __init__(self):
        moves = [
            Move("Poison jab", "POISON", 60),
            Move("Sludge bomb", "POISON", 80),
            Move("X-Scissor", "BUG", 80),
            Move("Infestation", "BUG", 0)
        ]
        super().__init__("Beedrill", 65, moves, "./TVPoke/Pokemon/imgs/Beedrill.png")