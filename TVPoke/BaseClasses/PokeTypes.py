from TVPoke.BaseClasses.PokeParentClass import Pokemon

class Water(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "WATER", "ELECTRIC", moves, imgPath)

class Ground(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GROUND", "GRASS", moves, imgPath) 

class Grass(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GRASS", "FIRE", moves, imgPath) 

class Fire(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "FIRE", "WATER", moves, imgPath)

class Electric(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "ELECTRIC", "GROUND", moves, imgPath)

class Normal(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "NORMAL", "FIGHT", moves, imgPath)
class Fighting(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "FIGHTING", "PSYCIC", moves, imgPath)

class Psychic(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "PSYCHIC", "DARK", moves, imgPath)

class Ghost(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GHOST", "GHOST", moves, imgPath)
        
class Bug(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "BUG", "FIRE", moves, imgPath)

class Poison(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "POISON", "GROUND", moves, imgPath)
        
class Dark(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "DARK", "BUG", moves, imgPath)

class Ice(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "ICE", "FIRE", moves, imgPath)

class Dragon(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "DRAGON", "DRAGON", moves, imgPath)

class Flying(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "FLYING", "ELECTRIC", moves, imgPath)

