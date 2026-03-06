from TVPoke.BaseClasses.Move import Move
from TVPoke.BaseClasses.PokeTypes import Normal

class Meowth(Normal):
    def __init__(self):
        moves = [
            Move("Scratch", "NORMAL", 40),
            Move("Bite", "DARK", 50),
            Move("Feint Attack", "DARK", 60),
            Move("Slash", "NORMAL", 40),
            Move("Payday", "NORMAL", 40)
        ]
        super().__init__("Meowth", 80, moves, "./TVPoke/Pokemon/imgs/meowth.png")