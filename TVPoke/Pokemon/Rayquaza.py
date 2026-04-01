from TVPoke.BaseClasses.PokeTypes import Dragon
from TVPoke.BaseClasses.Move import Move

class Rayquaza(Dragon):
    def __init__(self):
        moves = [
            Move("Volt Tackle", "ELECTRIC", 120),
            Move("Iron Tail", "ELECTRIC", 100),
            Move("Quick Attack", "ELECTRIC", 40),
            Move("Volt Thunderbolt", "ELECTRIC", 195)
        ]
        super().__init__("Rayquaza", 95, moves, "./TVPoke/Pokemon/imgs/Rayquaza.png")