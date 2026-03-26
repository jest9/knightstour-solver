"""
tiebreak algorithm (roth tiebreak)
"""

import random


def roth(move_list, size):

    # find central point

    c = 0


    center = ((size - 1) / 2, (size - 1) / 2)


    y = 0
    for i in move_list:
        # find distance from central point
        distance = ((i[0] - center[0]) ** 2 + (i[1] - center[1]) ** 2) ** 0.5 # get euclidean distance from central point
        #print("distance from central point for move", i, "is: ", distance)
        if y == 0:
            y = distance
            best_move = i
        elif distance > y:
            y = distance
            best_move = i
        elif distance == y:
            best_move = random.choice(move_list)
            
    return best_move, c



    # clean up code and add comments
