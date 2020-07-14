


#if(x is false):
reserveItems = [
    ':' , 'end' , '@main' , 'pb' , 'exts' , 
    'pv' , 'prot' , 'en' , '\'','const' , 'print' , 'println' , 'err.print'
    ]

replaseList = ['{' , '}' , 'public static void main', 'public' , 
    'extends' , 'private' , 'protected' , '}' , '"' , 'final' , 'System.out.print' , 'System.out.println'
    'System.err.print'
    ]

newLine = ''

def replaseManager (line):
    global newLine
    newLine = line
    for reservePosition in range(len(reserveItems)):
        if line.find(reserveItems[reservePosition]) != -1:
            newLine = newLine.replace(reserveItems[reservePosition] , replaseList[reservePosition])

    return newLine

#public static void main(String args[]) {}
#replaseManager('__main__(String args[]): end')
