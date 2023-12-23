from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

def aStar_with_costs(m, start=None, cost1_func=None, cost2_func=None, costT_func=None):
    if start is None:
        start = (m.rows, m.cols)

    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath = []

    lastCell = start
    fwdPath = {}
    Costs = {n: [100000.0, 100000.0, 100000.0] for n in m.grid}
    Costs[start] = [0, 0, 0]
    while not open.empty():
        
        currCell = open.get()[2]
        
            # If not in the list, then add it
        # fwdPath[searchPath[-1]] = currCell
        searchPath.append(currCell)
        # fwdPath[lastCell] = currCell
        lastCell = currCell

        if currCell == m._goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)
                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))

                    Costs[childCell] = [g_score[childCell], h(childCell, m._goal), f_score[childCell]]
    # print(searchPath)
    return searchPath, Costs, 0
