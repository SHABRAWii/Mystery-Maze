# Heuristic Function (h):

------------
- A* (A-star) is a popular pathfinding algorithm that combines Dijkstra's algorithm with a heuristic to find the shortest path in a graph. It evaluates nodes based on a combination of the cost to reach them and an estimated cost to reach the goal, making it efficient for navigation and robotics applications. The algorithm guarantees an optimal solution when the heuristic is admissible.

- The script defines a heuristic function h(cell1, cell2) that calculates the Manhattan distance between two cells. This function estimates the cost from one cell to another.
## 1. A Algorithm Function (aStar_with_costs):*

------------


- The aStar_with_costs function takes a maze (m), a starting position (defaulting to the bottom-right corner if not provided), and optional cost functions (cost1_func, cost2_func, costT_func).

- Initialize the priority queue (open) with the starting cell, and dictionaries (aPath, g_score, f_score) to store the paths, the cost from the start, and the estimated total cost, respectively.

- Initialize searchPath to keep track of the sequence of cells explored.

- The A* algorithm is executed within a loop until the priority queue is empty or the goal is reached.

- For each valid neighboring cell, calculate tentative g and f scores. If the tentative f score is lower than the existing f score for the cell, update the scores and add the cell to the priority queue.

- Calculate costs for specific cells during traversal and pass them to the respective cost functions (cost1_func, cost2_func, costT_func).

- Reconstruct the forward path from the goal to the start using the aPath dictionary.

- Return the sequence of explored cells (searchPath), the backward path (aPath), and the forward path (fwdPath).

## 2. Cost Functions (cost1_function, cost2_function, costT_function):

------------


- Example functions that print the costs associated with specific cells. These functions are called during the A* algorithm execution.
## 3. Main Section:

------------


- Create a 4x4 maze and load a maze configuration from a file named 'aStardemo.csv'.

- Call the aStar_with_costs function with cost functions for demonstration.

- Create three agents (a, b, and c) with different characteristics in the maze.

- Trace and visualize the paths of the agents using the traced paths with delays between each step.

- Display text labels indicating the lengths of the A* search and path.

- Run the maze simulation to observe the movements of the agents according to the traced paths.
- The A*(A-star) is the best algorithm to reeach the goal.

In summary, the script demonstrates the A* algorithm with costs in a maze environment. Cost functions are used to handle costs associated with specific cells during the A* traversal, and the script visualizes the paths taken by agents in the maze.