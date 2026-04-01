from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class Oddish(Grass):
    def __init__(self):
        moves = [
            Move( "Petal Dance" , "GRASS" , 120),
            Move( "Solar Beam" , "GRASS" , 120),
            Move( "Sludge Bomb" , "POISON" , 90),
            Move( "Energy Ball" , "GRASS" , 90)
        ]
        super().__init__("Oddish", 90, moves, "./TVPoke/Pokemon/imgs/Oddish.png")