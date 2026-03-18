"""
tiebreak algorithm (roth tiebreak)
"""

def roth(move_list, grid):

    # find central point
    if len(grid) % 2 != 0:
        middleIndex = (len(grid) - 1)/2
        midIndex = int(middleIndex)
        print(grid[midIndex])

    y = 0
    for i in move_list:
        # find distance from central point
        distance = ((i[0] - grid[midIndex][0]) ** 2 + (i[1] - grid[midIndex][1]) ** 2) ** 0.5 # get euclidean distance from central point
        print("distance from central point for move", i, "is: ", distance)
        if y == 0:
            y = distance
            best_move = i
        elif distance > y:
            y = distance
            best_move = i

            # add for even grid size
            


    print("best move is: ", best_move, "with distance: ", y)
    return best_move
