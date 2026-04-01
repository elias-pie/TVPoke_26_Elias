from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
import time

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (50, 162, 168))
        
        self.state = {
            "goTo": '',
            "ded": '',
            "Win": '',
            "Winner": ''
        }

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke, 1),
            Trainer(trainer2Poke, 2)
        ]

    def changeturn(self):
        self.trainers[1].removeFaintedPokemon()
        self.trainers[0].removeFaintedPokemon()
        if len(self.trainers[0].pokemon) == 0 or len(self.trainers[1].pokemon) == 0:
            self.state['ded'] = "ded"
        if len(self.trainers[0].pokemon) == 0 or len(self.trainers[1].pokemon) == 0:
            for i in self.trainers:
                print(i.myId)
            self.state['goTo'] = "WinScreen"

            if len(self.trainers[0].pokemon) == 0:
                self.state['Winner'] = self.trainers[1].myId
                print('Trainer @ id 1 won')
            elif len(self.trainers[1].pokemon) == 0:
                print('Trainer @ id 0 won')
                self.state['Winner'] = self.trainers[0].myId
        self.trainers.reverse()
    def elementsToDisplay(self):
        self.elements = [
            Label((50, 90), 20, 10, ''),
            ActiveIndicator((10, 90), 25, 5, 'Active Trainer: '+str(self.trainers[0].myId), 13, (255, 255, 255), (235, 64, 52)),
            Image((50, 75), 20, 20, './imgs/vs.png'),
            Rectangle((90, 5), 18, 4, (222, 227, 82)),
            Rectangle((15, 5), 18, 4, (222, 227, 82)),
            Label((90, 5), 20, 10, 'Being Attacked'),
            Label((15, 5), 20, 10, 'Attacker'),
        ]
        positionForPokes = 1
        pokemonID = 0
        trainerPokemonImage = []
        for trainer in self.trainers:
            x = 0
            y = 100
            xTwo = 50
            yTwo = 0
            if (positionForPokes == 1):
                    x = 15
            elif (positionForPokes == 2):
                    x = 90
            else:
                print('\033[31m====================================================================================') 
                print('An Unknown Error Occured. TRIGGER=C3_1' + "RelatedVars: [positionForPokes:"+str(positionForPokes)+']')                      #C3_3 = Component 3 (BattleScreen.py), Function 3 (elementsToDisplay)
                print('\033[31m====================================================================================\033[0m') 
                quit()
            for poke in trainer.pokemon:
                y -= 25
                self.elements.append(PokemonImage((x, y), 20, 20, poke.img, pokemonID))
                self.elements.append(Rectangle((x, y - 10), 18, 4, (255, 255, 255)))
                self.elements.append(Label((x, y - 10), 20, 10, poke.name + ' - HP: '+ str(poke.hp)))
                trainerPokemonImage.append((pokemonID, positionForPokes))
                pokemonID += 1
            positionForPokes += 1
        if self.state['ded'] == "": 
            buttonPos = [[42, 41], [59, 41], [42, 29], [59, 29]]
            for move in self.trainers[0].pokemon[0].moves:    
                moveIndex = self.trainers[0].pokemon[0].moves.index(move)
                self.elements.append(Pokemove((buttonPos[moveIndex][0], buttonPos[moveIndex][1]), 15, 10, move, (255, 255, 255), (0, 0, 0)))

class Pokemove(Button):
    def __init__(self, centerXY, width, height, move, textColorRGB=..., backColorRGB=...):
        self.move = move
        super().__init__(centerXY, width, height, move.name, textColorRGB, backColorRGB)
    def onClick(self, screen):
        screen.trainers[1].pokemon[0].takeDamage(self.move)
        screen.changeturn()

class PokemonImage(Image):
    def __init__(self, centerXY, width, height, imagePath, pokeID):
        super().__init__(centerXY, width, height, imagePath)
        self.pokeID = pokeID
        self.centerXY = centerXY
        
    def onClick(self, screen):
        pass

class ActiveIndicator(Label):
    def __init__(self, centerXY, width, height, text, fontSize=14, textColorRGB=..., backColorRGB=False):
        super().__init__(centerXY, width, height, text, fontSize, textColorRGB, backColorRGB)

class SwapPoke(Button):
    def __init__(self, centerXY, width, height, text, textColorRGB=..., backColorRGB=...):
        super().__init__(centerXY, width, height, text, textColorRGB, backColorRGB)
