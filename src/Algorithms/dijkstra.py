
def dijkstra(m, start=None, cost1_func=None, cost2_func=None, costT_func=None):
    if start is None:
        start = (m.rows, m.cols)

    # hurdles = [(i.position, i.cost) for i in h]

    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    fwdPath = {}
    lastCell = start
    TotalCost = 10
    Costs = {n: [None, None, float('999')] for n in m.grid}
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
                # for hurdle in hurdles:
                    # if hurdle[0] == currCell:
                        # tempDist += hurdle[1]
################################################################################
                # EDIT WE MADE (LABIB - ALAA)
                # cost1 = None
                # cost2 = None
                # costT = 0.0
                # if(currCell != start):
                #     rounded_Cells = [(currCell[0], currCell[1]+1),
                #                     (currCell[0], currCell[1]-1),
                #                     (currCell[0]+1, currCell[1]),
                #                     (currCell[0]-1, currCell[1]),
                #                     ]
                #     cost2 = None
                #     cost1 = None

                #     costs_list = [
                #         Costs.get((currCell[0], currCell[1]+1), [None, None, float('10000000')])[2],
                #         Costs.get((currCell[0], currCell[1]-1), [None, None, float('10000000')])[2],
                #         Costs.get((currCell[0]+1, currCell[1]), [None, None, float('10000000')])[2],
                #         Costs.get((currCell[0]-1, currCell[1]), [None, None, float('10000000')])[2]
                #     ]
                    # if costs_list:
                        # costT = 1 + min(costs_list + [10000000])
                        # if(costT > 900):
                            # print("hello, , ", costT)
                # if childCell == h1.position:
                    # cost1 = tempDist
                # elif childCell == h2.position:
                #     cost2 = tempDist


                # EDIT WE MADE
                # if cost1_func and cost1 is not None:
                #     cost1_func(cost1)
                # if cost2_func and cost2 is not None:
                #     cost2_func(cost2)
                # if costT_func and costT is not None:
                #     costT_func(costT)
                if tempDist < unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell
                    costT = 1 + Costs[currCell][2]

                # Costs[childCell] = [cost1, cost2, costT]

################################################################################
                    
        unvisited.pop(currCell)

    # fwdPath = {}
    # cell = m._goal
    # while cell != start:
    #     fwdPath[revPath[cell]] = cell
    #     cell = revPath[cell]
    # for i in range(1, 11):
    #     for j in range(1, 11):
    #         print(Costs[(i, j)][2], end=", ")
    #     print()
    return fwdPath, Costs, TotalCost
#--------------------------------------------------------------------------------
# Example functions for Cost1, Cost2, Cost total -- (ZAHRAN CODE)
def cost1_function(cost):
    print(f"Cost1 at bottom right: {cost}")

def cost2_function(cost):
    print(f"Cost2 at bottom left: {cost}")

def costT_function(cost):
    print(f"Cost Total at Center: {cost}")
#--------------------------------------------------------------------------------

# if __name__ == '__main__':
    # myMaze = maze(10, 15)
    # myMaze.CreateMaze(1, 4, loopPercent=100)

    # h1 = agent(myMaze, 4, 4, color=COLOR.red)
    # h2 = agent(myMaze, 4, 6, color=COLOR.red)
    # h3 = agent(myMaze, 4, 1, color=COLOR.red)
    # h4 = agent(myMaze, 4, 2, color=COLOR.red)
    # h5 = agent(myMaze, 4, 3, color=COLOR.red)

    # h1.cost = 100
    # h2.cost = 100
    # h3.cost = 100
    # h4.cost = 100
    # h5.cost = 100

    # # Pass the Cost functions to dijkstra_with_costs
    # path, c = dijkstra(
    #     myMaze, h1, h2, h3, h4, h5, start=(6, 1),
    #     cost1_func=cost1_function,
    #     cost2_func=cost2_function,
    #     costT_func=costT_function
    # )

    # a = agent(myMaze, 6, 1, color=COLOR.cyan, filled=True, footprints=True)
    # myMaze.tracePath({a: path})

    # myMaze.run()
