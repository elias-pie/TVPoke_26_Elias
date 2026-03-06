from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Flareon(Fire):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Ember", "Fire", 70),
            Move("Fire Fang", "Fire", 50),
            Move("Lava plume", "Fire", 90)
        ]
        super().__init__("Flareon", 80, moves, "./TVPoke/Pokemon/imgs/Flareon.png")