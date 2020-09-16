from mazeGenerator import Cell, createMaze
from time import sleep
from Printer import printMaze

'''
    Parameters
'''
width = 40
height = 30
startPoint = [0, 0]
endPoint = [width - 1, height - 1]

displaySolution = True
displayPath = False

def distanceOptimisation(walls, w, h):
    '''
        Gets the minimum distance to the endPoint to help the algorithm
        find the path within less iterations
    '''
    walls.append([abs(w - endPoint[0]) + abs((h - 1) - endPoint[1]), abs((w + 1) - endPoint[0]) + abs((h) - endPoint[1]), abs(w - endPoint[0]) + abs((h + 1) - endPoint[1]), abs((w - 1) - endPoint[0]) + abs((h) - endPoint[1])])
    minWalls = 100000
    smaller = 0
    for i in range(4):
        if (walls[i] == True and walls[4][i] < minWalls):
            minWalls = walls[4][i]
            smaller = i
    return smaller

def DepthFirstSearch(maze, w, h, display = False):
    '''
        Uses the depth first search algorithm to check all the cells
        until the endpoint is finished

        The path is kept in the same name array, each visited cells'
        coordinates are added in the path array when entering the cell
        and poped if the path doesn't lead anywhere
    '''
    if display == True:
        printMaze(maze, path, height, width)
        # sleep(0.01) # Can be usefull for bigger configs

    path.append([str(w), str(h)])
    maze[w][h].visited = 0

    if (w == endPoint[0] and h == endPoint[1]):
        return 1
    walls = [maze[w][h].north == 0 and h - 1 >= 0 and maze[w][h - 1].visited == 1, maze[w][h].east == 0 and w + 1 < width and maze[w + 1][h].visited == 1, maze[w][h].south == 0 and h + 1 < height and maze[w][h + 1].visited == 1, maze[w][h].west == 0 and w - 1 >= 0 and maze[w - 1][h].visited == 1]
    if sum(walls) == 0:
        return 0
    smaller = distanceOptimisation(walls, w, h)

    # Applies the algorithm for the smallest distance parameter
    if (DepthFirstSearch(maze, w + (smaller == 1) - (smaller == 3), h - (smaller == 0) + (smaller == 2), display) == 1):
        return (1)
    else:
        path.pop(-1)

    # Applies the algorithm until all paths are checked
    if (DepthFirstSearch(maze, w, h, display) == 1):
        return (1)
    else:
        path.pop(-1)


path = []
maze = createMaze(height, width, display = False)
DepthFirstSearch(maze, startPoint[0], startPoint[1], display = displayPath)
if (displaySolution):
    printMaze(maze, path, height, width)
