"""
logic docstring
"""

from tie_break import roth
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
    warns_move = []
    
    # random starting point
    random_start = random.choice(grid)

    used_moves.append(random_start)  # Starting point
    point = random_start

    # find valid moves
    
    # check if move is valid
    x = 1
    while True:
        for move in knight_moves:
            new_x = point[0] + move[0]
            new_y = point[1] + move[1]
            if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                valid_moves.append((new_x, new_y))
    
    # select move randomly from valid moves
        if not valid_moves:
            x = 0
            return used_moves  # No more valid moves

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

                print("total moves from", i, "is: ", y)
                if j == 0:
                    j = y
                    warns_move = i
                elif y < j:
                    tie_list.clear()
                    print(tie_list)
                    tie_list.append(i)
                    print(tie_list)
                    j = y
                    warns_move = i
                elif y == j:
                    tie_list.append(i)
                    print(tie_list)
        else:
            warns_move = valid_moves[0]
            
        # heuristic end

        if len(tie_list) == 0:
            print("end of tour")
        elif len(tie_list) == 1:
            warns_move = tie_list[0]
        elif len(tie_list) > 1:
            warns_move = roth(tie_list, grid)

        tie_list.clear()

        print("warns_move: ", warns_move)

        valid_moves.clear()
        point = warns_move
        used_moves.append(warns_move)


        



        

        



        