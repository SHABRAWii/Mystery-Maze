def dijkstra(m, start=None, cost1_func=None, cost2_func=None, costT_func=None):
    if start is None:
        start = (m.rows, m.cols)
    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    fwdPath = {}
    lastCell = start
    TotalCost = 10
    Costs = {n: [None, None, float('100000')] for n in m.grid}
    Costs[start] = [None, None, 0]
    while unvisited:
        currCell = min(unvisited, key=unvisited.get)
        fwdPath[lastCell] = currCell
        lastCell = currCell
        visited[currCell] = unvisited[currCell]
        if currCell == m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if childCell in visited:
                    continue
                tempDist = unvisited[currCell] + 1
                Costs[childCell] = [None, None, tempDist]
                if tempDist < unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell                
        unvisited.pop(currCell)
    return fwdPath, Costs, TotalCost