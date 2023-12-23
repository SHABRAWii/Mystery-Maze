from collections import deque
def BFS_with_costs(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch = []

    fwdPath = []
    Costs = {n: [None, None, float('100000')] for n in m.grid}
    Costs[start] = [None, None, 0]
    costWalk = 0
    while len(frontier) > 0:
        currCell = frontier.popleft()
        fwdPath.append(currCell)
        Costs[currCell] = [None, None, costWalk]
        costWalk = costWalk + 1
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)

    return fwdPath, Costs, 0