from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Jolteon(Electric):
    def __init__(self):
        moves=[
            Move('Thunder','ELECTRIC', 110),
            Move("Literal Joke Move", "NORMAL", 0),
            Move("Quick Attack", "NORMAL", 50),
            Move("Pound", "NORMAL", 40),
            
        ]
        super().__init__("Jolteon",140, moves,  "./TVPoke/Pokemon/imgs/Jolteon.png")
