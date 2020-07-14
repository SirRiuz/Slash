
reserve = [':']

def addEndPont (line):
    for item in reserve:
        if line[len(line) - 1] != item:
            return line[:-1] + ';'
        else:
            return line
