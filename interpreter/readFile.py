
from interpreter.replaseCharacters import replaseManager
from interpreter.methodsManager import  methods
from interpreter.interpreteManager import interpretateText

class fileReader (object):

    reservateArray = ['__main__' , ':']
    reservateArrayValues = ['public static void main' , '{']

    def __init__(self , fileDir):
        self.readFile(fileDir)

    def readFile (self , fileDir):
        try:
            file = open(fileDir , 'r')
            javaFileManager = open('javaFile.java' , 'w')
            for line in file:
                #print(line + '.')
                javaFileManager.write(self.AnalisateLine(line))
                print(self.AnalisateLine(line))

            file.close()
            javaFileManager.close()
        except Exception as e:
            print(e.message)


    def AnalisateLine(self , line):
        return interpretateText(line)
    #if(x is true):
    #if (x==true) {

