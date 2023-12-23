def DFS_with_costs(m, start=None, expand_func=None):
    if start is None:
        start = (m.rows, m.cols)

    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []
    fwdPath = []
    Costs = {n: [None, None, float('100000')] for n in m.grid}
    Costs[start] = [None, None, 0]
    costWalk = 0
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)
        fwdPath.append(currCell)
        Costs[currCell] = [None, None, costWalk]
        costWalk = costWalk + 1

        if currCell == m._goal:
            break

        poss = 0
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    child = (currCell[0] + 1, currCell[1])

                if child in explored:
                    continue

                poss += 1
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell

        if poss > 1:
            m.markCells.append(currCell)
    return fwdPath, Costs, 0
