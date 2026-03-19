"""
tiebreak algorithm (roth tiebreak)
"""

import random


def roth(move_list, grid):

    # find central point
    if len(grid) % 2 != 0:
        middleIndex = (len(grid) - 1)/2
        midIndex = int(middleIndex)
        #print(grid[midIndex])

        y = 0
        for i in move_list:
            # find distance from central point
            distance = ((i[0] - grid[midIndex][0]) ** 2 + (i[1] - grid[midIndex][1]) ** 2) ** 0.5 # get euclidean distance from central point
            #print("distance from central point for move", i, "is: ", distance)
            if y == 0:
                y = distance
                best_move = i
            elif distance > y:
                y = distance
                best_move = i
            elif distance == y:
                best_move = random.choice(move_list)

            # add for even grid size
    elif len(grid) % 2 == 0:
        middleIndex1 = (len(grid) - 1)/2
        middleIndex2 = middleIndex1 + 1
        midIndex1 = int(middleIndex1)
        midIndex2 = int(middleIndex2)
        central_points = [grid[midIndex1], grid[midIndex2]]
        #print("central points: ", central_points)

        y = 0
        for i in move_list:
            # find distance from central points
            distance1 = ((i[0] - grid[midIndex1][0]) ** 2 + (i[1] - grid[midIndex1][1]) ** 2) ** 0.5 # get euclidean distance from central point 1
            distance2 = ((i[0] - grid[midIndex2][0]) ** 2 + (i[1] - grid[midIndex2][1]) ** 2) ** 0.5 # get euclidean distance from central point 2
            distance = min(distance1, distance2) # take the minimum distance from the two central points
            #print("distance from central points for move", i, "is: ", distance)
            if y == 0:
                y = distance
                best_move = i
            elif distance > y:
                y = distance
                best_move = i
            elif distance == y:
                best_move = random.choice(move_list)
            


    #print("best move is: ", best_move, "with distance: ", y)
    return best_move
