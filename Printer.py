'''
    Basic Ascii Printer for the maze
    Uses a buffer that is then dumped for efficiency
'''

def printFirstLine(i, maze, printer, width):
    printer.append(["+"])
    for j in range(width):
        if (maze[j][i].north == 1):
            printer[-1].append('-')
            printer[-1].append('-')
            printer[-1].append('-')
        else:
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
        printer[-1].append('+')
    return printer

def printMiddleLine(i, maze, path, printer, width):
    printer.append([''])
    for j in range(width):
        printing = 0
        for index in range(len(path)):
            if (str(i) == path[index][1] and str(j) == path[index][0]):
                printing = 1
        if (maze[j][i].west == 1):
            if printing == 0:
                printer[-1].append('|')
                printer[-1].append(' ')
                printer[-1].append(' ')
                printer[-1].append(' ')
            else:
                printer[-1].append('|')
                printer[-1].append(' ')
                printer[-1].append('o')
                printer[-1].append(' ')
        elif printing == 1:
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append('o')
            printer[-1].append(' ')
        else:
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
    printer[-1].append('|')
    return printer

def printSecondLine(i, maze, printer, width):
    printer.append([''])
    for j in range(width):
        if (maze[j][i].west == 1):
            printer[-1].append('|')
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
        else:
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
            printer[-1].append(' ')
    printer[-1].append('|')
    return printer

def printLastLine(printer, width):
    printer.append([''])
    for i in range(width):
        printer[-1].append('+')
        printer[-1].append('-')
        printer[-1].append('-')
        printer[-1].append('-')
    printer[-1].append('+')
    return printer

def displayPrinter(printer):
    for item in printer:
        print(''.join(item))


def updatePath(maze, path, prevPath, h, w, printer):
    if (prevPath == 0):
        printer[2 * h + 1][3 + 4 * w] = ' '
    else:
        printer[2 * h + 1][3 + 4 * w] = 'o'
    displayPrinter(printer)
    return printer

def updateWalls(maze, prevCell, h, w, printer):
    if (prevCell == 1):
        printer[2 * h][1 + 4 * w] = ' '
        printer[2 * h][2 + 4 * w] = ' '
        printer[2 * h][3 + 4 * w] = ' '
    elif (prevCell == 2):
        printer[2 * h + 1][5 + 4 * w] = ' '
    elif (prevCell == 3):
        printer[2 * (h + 1)][1 + 4 * w] = ' '
        printer[2 * (h + 1)][2 + 4 * w] = ' '
        printer[2 * (h + 1)][3 + 4 * w] = ' '
    elif (prevCell == 4):
        printer[2 * h + 1][1 + 4 * w] = ' '
    displayPrinter(printer)
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
    displayPrinter(printer)
    return printer
