from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Grimer(Poison):
    def __init__(self):
        moves = [
            Move("Crunch", "NORMAL", 40),
            Move("Poison Jab", "POISON", 40),
            Move("Acid Armor", "POISON", 80),
            Move("Mud Bomb", "GROUND", 0)
        ]
        super().__init__("Grimer", 80, moves, "./TVPoke/Pokemon/imgs/Grimer.png")