"""
logic docstring
"""

from draw import draw_pattern
from tie_break import roth
import itertools


def grid_logic(var1, surface, grid_coordinates):
    grid = list(itertools.product(range(var1), range(var1)))
    usedmoves = move_logic(surface, var1, grid, grid_coordinates)
    return usedmoves


def move_logic(surface, var1, grid, grid_coordinates):

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    used_moves = set() # used moves stored in a set for O(1) lookup
    warns_move = []
    
    # starting point
    start = grid[0]

    used_moves.add(start)
    point = start

    draw_pattern(surface, var1, start, grid_coordinates)

    # find valid moves

    x = 1
    while True:
        for move in knight_moves:
            new_x = point[0] + move[0]
            new_y = point[1] + move[1]
            if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                valid_moves.append((new_x, new_y))

        if not valid_moves: # no more valid moves
            x = 0
            print("moves made =", len(used_moves), "out of", len(grid))
            return

        j = 0
        
        # basic warnsdorff implementation
        
        tie_list = []

        if len(valid_moves) >= 1:
            
            # move with least onward moves

            for i in valid_moves:
                y = 0
                for move in knight_moves:
                    new_x = i[0] + move[0]
                    new_y = i[1] + move[1]
                    if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                        y = y + 1

                if j == 0:
                    j = y
                    warns_move = i
                elif y < j:
                    tie_list.clear()
                    tie_list.append(i)
                    j = y
                    warns_move = i
                elif y == j:
                    tie_list.append(i)
        else:
            warns_move = valid_moves[0]
            
        # heuristic ending

        if len(tie_list) > 1:
            warns_move = roth(tie_list, grid)

        tie_list.clear()

        valid_moves.clear()
        point = warns_move

        print(warns_move)
        used_moves.add(warns_move)

        draw_pattern(surface, var1, warns_move, grid_coordinates)


        



        

        



        