# DFS Algorithm function:

------------
- Depth-First Search (DFS) is a graph traversal algorithm that explores as deeply as possible along each branch before backtracking. Using a stack or recursion, it visits a node, explores its unvisited neighbors, and continues until it reaches the deepest level before backtracking. DFS is employed in tasks such as topological sorting, maze solving, and connected component identification.
- DFS is the third best algorithm to find the goal.
## 1. Initialization:

------------

The script starts by defining a DFS function (DFS_with_costs) that performs Depth-First Search on a maze with the option to associate costs with specific cells. The function takes the maze (m), a starting position (defaulting to the bottom-right corner if not provided), and an expand function.
## 2. Data Structures:

------------

Initialize data structures: explored to track explored cells, frontier as the stack for DFS traversal, dfsPath to store the backward path, and dSearch to record the sequence of cells explored.
## 3. DFS Traversal Loop:

------------

While the stack (frontier) is not empty, pop a cell from the stack (currCell) and record it in the sequence of explored cells (dSearch).
## 4.  Neighboring Cell Exploration:

------------

For each valid direction ('E', 'S', 'N', 'W'), calculate the neighboring cell (child). If unexplored, add it to the stack and mark it as explored.
## 5. Marking Cells:

------------
If there are multiple possibilities from the current cell, mark the cell for visualization.
## 6. Cost Calculation and Expand Function:

-----------
Calculate costs for specific cells based on conditions. Pass the costs to the expand function, if provided. The expand function prints information about moving from an old cell to a new cell and associated costs.
## 7. Reconstruct Forward Path:

------------
Reconstruct the forward path from the goal to the start using the dfsPath dictionary.
## 8. Return Results:

------------
Return the sequence of explored cells (dSearch), the backward path (dfsPath), and the forward path (fwdPath).

## 9. Expand Function:

------------
Example implementation of the expand function that prints information about the movement and associated costs during DFS traversal.
## 10. Main Section:

------------
In the main section, create a maze of a specified size and with a designated goal cell.
- DFS with Costs:
Perform DFS with costs on the maze, starting from a specified cell, and using the provided expand function.
- Agent Initialization:
Create three agents (a, b, and c) with different characteristics in the maze.
- Trace Paths and Visualization:
Trace and visualize the paths of the agents using the traced paths.
- Run Simulation:
Run the maze simulation to observe the movements of the agents according to the traced paths.

In summary, the script explores a maze using Depth-First Search with the option to associate costs with specific cells. The expand function handles cost-related information, and the script visualizes the paths taken by agents in the maze.
