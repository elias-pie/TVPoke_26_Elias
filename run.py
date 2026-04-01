from PyUI.Window import Window
##import the custom screens you made---
from SelectScreen import SelectScreen
from BattleScreen import BattleScreen
from WinScreen import WinScreen
##-------------------------------------


window = Window("TVPoke26", (0,255,0), './imgs/pokeIcon.png') ##Create the window to work with

##Create Screen Objects for use------
selectScreen = SelectScreen(window)
battleScreen = BattleScreen(window)
##-----------------------------------

screen = selectScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if selectScreen.state["goTo"] == "BATTLE":
        pokemonList1 = selectScreen.state["selectedPoke"][0]
        pokemonList2 = selectScreen.state["selectedPoke"][1]
        battleScreen.addTrainers(pokemonList1, pokemonList2)
        selectScreen.state["goTo"] = ''
        screen = battleScreen
    if screen.state["goTo"] == 'WinScreen':
        trueWinner = 'Error'
        winner = screen.state["Winner"]
        print(winner)
        screen = WinScreen(window, winner)




    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
