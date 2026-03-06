from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Ninetails(Fire):
    def __init__(self):
        moves = [
            Move("Roar", "NORMAL", 80),
            Move("Ember", "FIRE", 80),
            Move("Fire Spin", "FIRE", 160),
            Move("Wil-O-Wisp", "FIRE", 160)
        ]
        super().__init__("Ninetails", 250, moves, "./TVPoke/Pokemon/imgs/Ninetails.png")