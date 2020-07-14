
reserveItems = ['' , '_' , '.']
replaseList = ['public' , 'private' , 'protected']
replaseHolder = ['static' , 'def' , 'const' , ' ']
returnManagerList = ['defconst' , 'def ' , 'defconststatic' , 'defstatic']
newLine = ''
defNewLine = ''

def returnManager (line):
    global defNewLine

    lineValue = ''
    for linePosition in range(len(line) , 0 , -1):
        if line[linePosition - 1] != ' ':
            #print(line[linePosition - 1])
            pass
        else:
            for x in range(linePosition , 0 , -1):
                lineValue += line[x - 1]
            # returnManagerList = ['defconst' , 'def' , 'defconststatic' , 'defstatic']
            for itemsPositions in (0 , returnManagerList):
                for item in returnManagerList:
                    if lineValue[::-1].replace(' ' , '') == 'defconst':
                        defNewLine = 'void'
                    elif lineValue[::-1].replace(' ' , '') == 'def':
                        defNewLine = 'void'
                    elif lineValue[::-1].replace(' ' , '') == 'defstatic':
                        defNewLine = 'void'
                    elif lineValue[::-1].replace(' ' , '') == 'defconststatic':
                        defNewLine = 'void'
                    else:
                        defNewLine = lineValue[::-1]
                        defNewLine = defNewLine.replace(replaseHolder[0] , '')
                        defNewLine = defNewLine.replace(replaseHolder[1] , '')
                        defNewLine = defNewLine.replace(replaseHolder[2] , '')
                        defNewLine = defNewLine.replace(replaseHolder[3] , '')

            break
    return defNewLine

def constManager (line):
    if line.find('const') != -1:
        return 'final {}'.format(line.replace('const' , ''))
    return line


def methods (line):
    position = 0
    global newLine
    newLine = line

    objectReturn = returnManager(line)
    if line.find('def') != -1:
        for positionItem in range(0,len(reserveItems)):
            if line.find(reserveItems[positionItem]) != -1:
                if reserveItems[positionItem] == '':
                    newLine = line.replace('def' , 'public ')

                if reserveItems[positionItem] == '_':
                    newLine = line.replace('def' , 'private ')

                if reserveItems[positionItem] == '.':
                    newLine = line.replace('def' , 'protected ')


        return constManager(newLine)
    else:
        return line

# def final static ovid  managerData()
print(methods('def cost static void master ():'))




