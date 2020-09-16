'''
    Basic Ascii Printer for the maze
    Uses a buffer that is then dumped for efficiency
'''

def printFirstLine(i, maze, printer, width):
    string = "+"
    for j in range(width):
        if (maze[j][i].north == 1):
            string += '---'
        else:
            string += '   '
        string += '+'
    printer.append(string)
    return printer

def printMiddleLine(i, maze, path, printer, width):
    string = ''
    for j in range(width):
        printing = 0
        for index in range(len(path)):
            if (str(i) == path[index][1] and str(j) == path[index][0]):
                printing = 1
        if (maze[j][i].west == 1):
            if printing == 0:
                string += '|   '
            else:
                string += '| o '
        elif printing == 1:
            string += '  o '
        else:
            string += '    '
    string += '|'
    printer.append(string)
    return printer

def printSecondLine(i, maze, printer, width):
    string = ''
    for j in range(width):
        if (maze[j][i].west == 1):
            string += '|   '
        else:
            string += '    '
    string += '|'
    printer.append(string)
    return printer

def printLastLine(printer, width):
    string = ''
    for i in range(width):
        string += '+---'
    string += '+'
    printer.append(string)
    return printer

def printMaze(maze, path, height, width):
    printer = []
    for i in range(height):
        printer = printFirstLine(i, maze, printer, width)
        if path == None:
            printer = printSecondLine(i, maze, printer, width)
        else:
            printer = printMiddleLine(i, maze, path, printer, width)
    printer = printLastLine(printer, width)
    for item in printer:
        print(item)
