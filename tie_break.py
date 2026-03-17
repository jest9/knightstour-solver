"""
tiebreak algorithm (roth tiebreak)
"""

import random
import time

def roth(move_list, grid):


    # find central point
    if len(grid) % 2 != 0:
        middleIndex = (len(grid) - 1)/2
        midIndex = int(middleIndex)
        print(grid[midIndex])

        # finish tomorrow


    return random.choice(move_list)
