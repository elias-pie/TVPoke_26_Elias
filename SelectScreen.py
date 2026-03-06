from PyUI.Screen import Screen
from PyUI.PageElements import *
from TVPoke.helper import getAllPokemonNames

class SelectScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (39, 115, 52))
        self.state = {
            "trainerIndex": 0,
            "selectedPoke": [[], []],
            "pageNum": 0,
            "allPokemon": getAllPokemonNames(),
            "pokemonShowing": [],
            "hasNextPage": False,
            "hasPrevPage": False,
            "goTo": "",
            "confirmed": False,
            "buttonText": "Confirm",
            "buttonColor": [(0,0,0), (255, 255, 255)]
        }
        self.updatePokemonShowing()


    def elementsToDisplay(self):
        self.elements = [ 
            Label((25, 95), 50, 10, "Choose your pokemon!\nPlayer " + str(self.state["trainerIndex"] + 1), 24),
            ConfirmButton((75, 5), 30, 8, self.state["buttonText"], self.state["buttonColor"][0], self.state["buttonColor"][1])
        ]
        itemsPerRow = 3
        rowsOfItems = 3


        #uses left part of screen for pokemon to select, right to show pokemon selected

        yCoord = 0
        indexOnPage = -1
        for y in range(rowsOfItems):
            xCoord = 0
            yCoord += 80/(rowsOfItems + 1)
            
            for x in range(itemsPerRow):
                indexOnPage += 1
                xCoord += 50/(itemsPerRow + 1)
                if indexOnPage < len(self.state["pokemonShowing"]):
                    self.elements.append(PokeImage((xCoord, yCoord), self.state["pokemonShowing"][indexOnPage], 50/(itemsPerRow + 1), 80/(rowsOfItems + 1)))
                else:
                    break

        if self.state["hasPrevPage"]:
            self.elements.append(BackButton())
        if self.state["hasNextPage"]:
            self.elements.append(ForwardButton())

        #uses right part of screen to show pokemon selected
        yCoord = 0
        for p in self.state["selectedPoke"][self.state["trainerIndex"]]:
            yCoord += 100/4
            self.elements.append(SelectedPokeImage((75, yCoord), p, 20, 100/4))
        if len(self.state["selectedPoke"][self.state["trainerIndex"]]) == 3 and self.state["confirmed"] == True:
            self.waitForNextFrame = 2
            self.elements.append(Label((75, 95), 50, 20, "Choosing Complete!", 30))
            self.state["confirmed"] = False
            if self.state["trainerIndex"] == 1:
                self.state["goTo"] = "BATTLE"
            else:
                self.state["trainerIndex"] += 1


    def updatePokemonShowing(self):
        startIndex = self.state["pageNum"] * 9
        self.state["hasPrevPage"] = startIndex > 0
        pokeShowing = []
        self.state["hasNextPage"] = True
        for i in range(startIndex, startIndex + 9):
            if i < len(self.state["allPokemon"]):
                pokeShowing.append(self.state["allPokemon"][i])
            else:
                self.state["hasNextPage"] = False
                break
        self.state["pokemonShowing"] = pokeShowing
                
class PokeImage(Image):
    def __init__(self, pos, name, width, height):
        self.name = name
        super().__init__(pos, width, height, './TVPoke/Pokemon/imgs/' + name + '.png')

    def onClick(self, screen):
        if (screen.state["trainerIndex"] == 0 and len(screen.state["selectedPoke"][0]) != 3):
            screen.state["selectedPoke"][screen.state["trainerIndex"]].append(self.name)
            screen.state["buttonText"] = 'Confirm'
            screen.state["buttonColor"][1] = (255, 255, 255)
        elif (screen.state["trainerIndex"] == 1 and len(screen.state["selectedPoke"][1]) != 3):
            screen.state["selectedPoke"][screen.state["trainerIndex"]].append(self.name)
            screen.state["buttonText"] = 'Confirm'
            screen.state["buttonColor"][1] = (255, 255, 255)
        else:
            screen.state["buttonText"] = 'Max of 3 is allowed!'
            screen.state["buttonColor"][1] = (245, 66, 69)


class SelectedPokeImage(Image):
    def __init__(self, pos, name, width, height):
        self.name = name
        super().__init__(pos, width, height, './TVPoke/Pokemon/imgs/' + name + '.png')

    def onClick(self, screen):
        screen.state["selectedPoke"][screen.state["trainerIndex"]].remove(self.name)
        screen.state["buttonText"] = 'Confirm'
        screen.state["buttonColor"][1] = (255, 255, 255)


class BackButton(Image):
    def __init__(self):
        super().__init__((5, 85), 10, 13, './imgs/btkBttn.png')

    def onClick(self, screen):
        screen.state["pageNum"] -= 1
        screen.updatePokemonShowing()

class ForwardButton(Image):
    def __init__(self):
        super().__init__((45, 85), 10, 13, './imgs/fwdBttn.png')

    def onClick(self, screen):
        screen.state["pageNum"] += 1
        screen.updatePokemonShowing()

class ConfirmButton(Button):
    def __init__(self, centerXY, width, height, text, textColorRGB=(0,0,0), backColorRGB=(255,255,255)):
        super().__init__(centerXY, width, height, text, textColorRGB, backColorRGB)

    def onClick(self, screen):
        if len(screen.state["selectedPoke"][0]) == 3:
            screen.state["confirmed"] = True
            print('ConfirmedPokemon')
        else:
            screen.state["buttonText"] = 'You need 3 pokes'
            screen.state["buttonColor"][1] = (245, 66, 69)
    
        
