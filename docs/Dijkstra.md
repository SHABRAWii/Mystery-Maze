# Dijkstra's Algorithm Function (dijkstra):

------------


- Dijkstra's Algorithm is a method for finding the shortest path between two points in a graph. It works with non-negative edge weights and iteratively explores the graph, updating the shortest distances. The algorithm is commonly used in route planning and network optimization.




- The dijkstra function is the second best algorithm

## The dijkstra function takes the following parameters:


## - Inputs:

------------


m: Maze object.
*h: Arbitrary number of hurdles.
start: Starting position (defaulting to the bottom-right corner if not provided).
cost1_func, cost2_func, costT_func: Optional cost functions.

### - Algorithm Steps:

------------


1. Extract hurdle positions and costs from the provided h arguments.
2. Initialize dictionaries (unvisited, visited, revPath) to keep track of unvisited cells, visited cells with their distances, and the reverse path.
3. Iterate until all cells are visited or the goal cell is reached.
4. For each neighboring cell, calculate tentative distances considering hurdles and update the distances and path if a shorter path is found.
5. Calculate costs for specific cells during traversal and pass them to the respective cost functions (cost1_func, cost2_func, costT_func).
6. Reconstruct the forward path from the goal to the start using the revPath dictionary.
7. Return the forward path (fwdPath) and the total cost to reach the goal (visited[m._goal]).

Cost Functions (cost1_function, cost2_function, costT_function):
Example functions that print the costs associated with specific cells. These functions are called during the Dijkstra's algorithm execution.

### - Main Section:

------------


1. Create a 10x15 maze with a 100% loopiness and set up the maze.
2. Create five agents (h1 to h5) as hurdles at different positions in the maze.
3. Assign a cost of 100 to each hurdle.
4. Call the dijkstra function with cost functions for demonstration, starting from the cell(6, 1).
5. Create an agent (a) with specific characteristics in the maze.
6. Trace and visualize the path of agent a using the traced path.
7. Run the maze simulation to observe the movements of the agent according to the traced path.

In summary, the script demonstrates Dijkstra's algorithm with costs in a maze environment. Cost functions handle costs associated with specific cells during the algorithm's traversal, and the script visualizes the path taken by an agent in the maze.











