#Main program - User Interface
import sys
sys.path.append('classes')
sys.path.append('imp')
from BoltFunctional import Bolt
from mBD import mockBD
from APIfuncional import apiTwitch
from basedatos import database


#Global setting variables
MOTHER_PATH = "saves\{}.txt"    #Static path name to save options for later
DEPTH = 1                       #How many layers it is going to calculate (op -> follower -> follower) for today only 1 layer deep
C_ACTIVITY = False              #Compute and ponder based on the channel activity
LIMIT_RECOMENDATIONS = 5        #How many channels its going to calculate; -1 for all
AVOID_BLOCKED = True            #Avoid blocked channels to recomendations (blocked and double recomendations)
DEBUG = True                    #If true, then print debug information to console

workingapi = apiTwitch()
coneccion_bd = database()
workingbolt = Bolt(workingapi, coneccion_bd)

def getOptions():
    return """
    1. Load Options
    2. Save Options
    3. Add channel
    4. Remove channel
    5. Block channel
    6. Calculate
    7. Get Recomendations
    8. View Channels
    9. Agregar por usuario
    0. Quit"""

def getChannel():
    print("Enter name of channel: ")
    chan = input(">> ")
    try:
        workingapi.get_userid(chan)
        return chan
    except:
        print("Hay un problema con este canal, o no hay internet")
        return -1

def takeAction():
    errors = 0
    ret = -1
    while(ret == -1):
        if errors == 3:
            print("\nTo many errors!\nHere are the options again:")
            print(getOptions())
            errors = 0

        try:
            #c = input("> ")
            c = int(input("> "))
            #DEBUG.append(c)
            if c <= -1 or c >= 10:
                print("Out of bounds!")
                c = -1
            ret = c
        except:
            print("Please only numbers!")

        errors += 1
    return c

def doAction(comand):
    if comand == 0:
        print("Goodbye!")
        return -1

    elif comand == 1:
        workingbolt.ls_channel = coneccion_bd.get_list()

    elif comand == 2:
        coneccion_bd.save_list(workingbolt.ls_channel)

    elif comand >= 3 and comand <= 5:
        channel = getChannel()
        if comand == 3:
            workingbolt.addChanel(channel)
        elif comand == 4:
            workingbolt.removeChanel(channel)
        else:
            workingbolt.blockChanel(channel)

    elif comand == 6:
        workingbolt.calculate()

    elif comand == 7:
        workingbolt.printRecomendations()

    elif comand == 8:
        workingbolt.viewChannels()

    elif comand == 9:
        name = getChannel()
        workingbolt.getFromUser(name)
    else:
        print("How did you got here? o.O")

def main(deb):
    print(getOptions())
    loop = True
    while(loop):
        com = takeAction()
        salir = doAction(com)
        
        if salir is not None:
            return
        if deb:
            loop = False

if __name__ == '__main__':
    main(False)
