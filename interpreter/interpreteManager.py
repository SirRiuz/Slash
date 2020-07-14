
from interpreter.andPoint import addEndPont
from interpreter.replaseCharacters import replaseManager
from interpreter.methodsManager import methods


def interpretateText (line):
    #replaseManager(addEndPont(line))
    return methods(replaseManager(addEndPont(line)))
    #print()