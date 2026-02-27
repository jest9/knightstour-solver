"""
logic docstring
"""

import time
import random
import itertools


def grid_logic(var1):
    grid = list(itertools.product(range(var1), range(var1)))
    usedmoves = move_logic(grid)
    return usedmoves


def move_logic(grid):

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    used_moves = []
    used_moves.append((0, 0))  # Starting point
    point = (0, 0)

    #find valid moves
    
    # check if move is valid
    x = 1
    while True:
        #print(point)
        #print(used_moves)
        time.sleep(1)
        for move in knight_moves:
            new_x = point[0] + move[0]
            new_y = point[1] + move[1]
            if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                #print("valid move: ", (new_x, new_y), "is not in used moves: ", used_moves)
                valid_moves.append((new_x, new_y))
    
    # select move randomly from valid moves
        if not valid_moves:
            x = 0
            return used_moves  # No more valid moves

        random_move = random.choice(valid_moves)
        valid_moves.clear()

        point = random_move
        used_moves.append(random_move)

        



        