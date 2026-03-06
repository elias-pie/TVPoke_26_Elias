from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Magikarp(Water):
    def __init__(self):
        moves = [
            Move("Bubble Beam", "WATER", 9999),
            Move("Aqua Jet", "WATER", 9999),
            Move("Crabhammer", "WATER", 9999),
            Move("Splash", "WATER", 0)
        ]
        super().__init__("Magikarp", 1000 * 1000, moves, "./TVPoke/Pokemon/imgs/Magikarp.png")