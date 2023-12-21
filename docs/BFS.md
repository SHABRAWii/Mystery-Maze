# BFS Algorthim function:

-----------
- Breadth-First Search (BFS) is a graph traversal algorithm that systematically explores the nodes of a graph level by level. It uses a queue to visit all neighboring nodes of the current level before moving on to the next level, making it suitable for finding the shortest path in an unweighted graph. BFS is commonly applied in network analysis and pathfinding.
- BFS is the third best algorithm to find the goal.

## 1. Initialization:

------------


- The script starts by importing necessary modules, including those from the PyAmaze library and the deque class for a double-ended queue.
## 2. BFS_with_costs Function:

------------

- A function named BFS_with_costs is defined to perform Breadth-First Search (BFS) on a maze with the option to associate costs with specific cells. The function takes the maze (m), a starting position (defaulting to the bottom-right corner if not provided), and an expand function.

- The function initializes data structures such as a deque (frontier), dictionaries (bfsPath for the path found by BFS), and lists (explored to track explored cells, bSearch to store the sequence of cells explored).

- A while loop runs until the frontier is empty or the goal is reached. Within the loop, the script explores neighboring cells in the four cardinal directions ('E', 'S', 'N', 'W').

- The backward path (bfsPath) is constructed, and the function returns the sequence of explored cells (bSearch), the backward path (bfsPath), and the forward path (fwdPath).

## 3. Expand Function:

------------


- An expand_func function is provided as an example implementation for handling costs during BFS. It prints information about moving from an old cell to a new cell and associated costs.
## 4.  Main Section:

------------

- The script enters the main section, where a maze with 12 rows and 10 columns is created using the PyAmaze library. The maze includes a 10% loopiness and follows a 'light' theme.

- BFS with costs is performed on the maze, and three agents (a, b, and c) are created with different characteristics, such as footprints, color, shape, and fill.

- The script then traces and visualizes the paths of the agents (a, b, and c) using the traced paths with delays between each step.

- Finally, the maze simulation is run, allowing the agents to move according to the traced paths.

In summary, the script initializes a maze, performs BFS with costs, creates agents, visualizes their paths, and runs a simulation to observe their movements in the maze. The expand function is called during BFS to handle costs associated with specific cells. The overall goal is to explore the maze efficiently while considering costs for certain cell traversals.