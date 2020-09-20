from random import randrange, seed
from time import sleep, time
from Printer import printMaze, updateWalls

# seed(8) # Sets a random seed value, can be used for debug
'''
    Parameters
'''
mazeDisplay = False
wallsDisplay = False

class Cell():
    '''
        Each cell represents a piece of the maze, each wall is represented by a direction 
    '''
    def __init__(self):
        self.north = 1
        self.south = 1
        self.west = 1
        self.east = 1
        self.visited = 0

    def set_coordinates(self, array):
        self.north = array[0]
        self.east = array[1]
        self.south = array[2]
        self.west = array[3]


    def get_coordinates(self):
        return [self.north, self.east, self.south, self.west]
    

def initMaze(height, width):
    ''' 
        Initialises the maze grid, with all walls up
        Theses walls will then one by one get removed by the algorithm to get the final maze
    '''
    maze = [[Cell() for j in range(height)] for i in range(width)]
    return maze

def createHoles(maze, w, h, prevCell, height, width, printer, display = False):
    ''' 
        Randomly breaks the walls of the grid to build the maze
        Uses recursivity to explore all the cells making sure the maze is "perfect"
    '''

    if display == True and wallsDisplay == True:
        printer = updateWalls(maze, prevCell, h, w, printer)

    maze[w][h].visited = 1

    # Removes wall where the previous cell was e.g. removes the north wall when coming from south
    if (prevCell != 0):
        coordinates = maze[w][h].get_coordinates()
        coordinates[prevCell - 1] = 0
        maze[w][h].set_coordinates(coordinates)

    # Walls : boolean array of each direction, used to know where to go next
    walls = [maze[w][h].north == 1 and h - 1 >= 0 and maze[w][h - 1].visited == 0, maze[w][h].east == 1 and w + 1 < width and maze[w + 1][h].visited == 0, maze[w][h].south == 1 and h + 1 < height and maze[w][h + 1].visited == 0, maze[w][h].west == 1 and w - 1 >= 0 and maze[w - 1][h].visited == 0]
    if sum(walls) == 0: # when all elements of walls are False
        return
    num = randrange(4) # randomizing which side to go
    while (walls[num] != True):
        num = randrange(4)
    
    # Launching recursives in different directions
    if (num == 0):
        maze[w][h].north = 0
        createHoles(maze, w, h - 1, 3, height, width, printer, display)
    if (num == 1):
        maze[w][h].east = 0
        createHoles(maze, w + 1, h, 4, height, width, printer, display)
    if (num == 2):
        maze[w][h].south = 0
        createHoles(maze, w, h + 1, 1, height, width, printer, display)
    if (num == 3):
        maze[w][h].west = 0
        createHoles(maze, w - 1, h, 2, height, width, printer, display)
    # Runs the same cell until all nieghbors are visited in different directions
    return createHoles(maze, w, h, 0, height, width, printer, display)

def createMaze(height, width, display = True):
    printer = []
    maze = initMaze(height, width)
    if (wallsDisplay == True and display == True):
        printer = printMaze(maze, None, height, width)
    createHoles(maze, 0, 0, 0, height, width, printer, display)
    if (mazeDisplay == True and display == True):
        printMaze(maze, None, height, width)
    return maze

if __name__ == "__main__":
    createMaze(30, 40)
