"""
logic docstring
"""

import itertools


def grid_logic(var1):
    grid = list(itertools.product(range(var1), range(var1)))
    for i in grid:
        print(i)
    return grid