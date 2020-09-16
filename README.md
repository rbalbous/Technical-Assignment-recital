# Technical-Assignment-recital

To launch the maze generator :
`python3 mazeGenerator.py`

This operation will generate a random maze.

To launch the maze solver :
`python3 mazeSolver.py`

This operation will generate a random maze grid and solve it.

To generate the maze I initialise a complete grid, I then use a recursive algorithm
to pass through all the cells and randomly break each wall to create paths.
I chose this solution because it is quick and very visual.

For the solver I implemented a recursive breadth first search algorithm that chooses the direction
based on the distance with the endpoint. 
The path is stored in an array, each node is added when we first check it, and they are deleted if the path
goes backward. When the enpoint is reached, each recursive function returns, leaving only in the path array
the informations we need.
I used this solution because it is very effecient in this case where we only have 1 correct path.
It's simple implementation was perfectly adapted to this project.

The visualization is made of ascii characters, and displayed on the standard output.

All the parameters and display options can be modified at the top of the files.
