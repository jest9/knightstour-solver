"""
tiebreak algorithm (roth tiebreak)
"""

import random
import time


def roth(move_list, size):

    # find central point

    c = 0


    center = ((size - 1) / 2, (size - 1) / 2)


    y = 0
    tie_list = []
    
    for i in move_list:
        # find distance from central point
        distance = ((i[0] - center[0]) ** 2 + (i[1] - center[1]) ** 2) ** 0.5 # get euclidean distance from central point
        
        if y == 0:
            y = distance
            best_move = i
            tie_list.append(i)
        elif y < distance:
            tie_list.clear()
            tie_list.append(i)
            y = distance
            best_move = i
        elif y == distance:
            tie_list.append(i)

    if len(tie_list) > 1:
        best_move = random.choice(tie_list)
        c = 1
        return best_move, c
    else:
        return best_move, c



    # clean up code and add comments
