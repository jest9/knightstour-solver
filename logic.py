"""
logic docstring
"""

from tie_break import roth
from stats import stats
import itertools
from config import headless_option, size
if headless_option == "0":
    from config import sample_surface



def grid_logic(size, grid_coordinates=False):

    grid = set(range(size * size)) # create a set of all possible grid coordinates

    if grid_coordinates != False:
        usedmoves = move_logic(grid, grid_coordinates)
    else:
        usedmoves = move_logic(grid, grid_coordinates=False, headless=True)
    return usedmoves


def move_logic(grid, grid_coordinates=False, headless=False):

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    used_moves = set() # used moves stored in a set for O(1) lookup
    warns_move = []
    tied_moves = 0
    random_tied_moves_increment = 0
    
    # starting point
    start = 0

    used_moves.add(start)
    point = start

    if (headless == True):
        pass
    else:
        from draw import draw_pattern
        draw_pattern(sample_surface, size, start, grid_coordinates)

    # find valid moves

    print("solving...")

    x = 1
    while True:
        px, py = divmod(point, size)
        for move in knight_moves:
            new_x = px + move[0]
            new_y = py + move[1]
            if 0 <= new_x < size and 0 <= new_y < size and (new_x * size + new_y) not in used_moves:
                valid_moves.append(new_x * size + new_y)



        if not valid_moves: # no more valid moves

            print("\nEnding tour...")

            stats(len(grid), len(used_moves), tied_moves, random_tied_moves_increment)

            break



        j = 0
        
        # basic warnsdorff implementation
        
        tie_list = []

        if len(valid_moves) >= 1:
            
            # move with least onward moves


            # probably can cut this down

            for i in valid_moves:
                y = 0
                ix, iy = divmod(i, size)
                for move in knight_moves:
                    new_x = ix + move[0]
                    new_y = iy + move[1]
                    if 0 <= new_x < size and 0 <= new_y < size and (new_x * size + new_y) not in used_moves:
                        y = y + 1

                if j == 0:
                    tie_list.append(i) # silly bugs
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
            warns_move, random_tied_moves_res = roth(tie_list, size)
            tied_moves += 1
            if random_tied_moves_res == 1:
                random_tied_moves_increment += 1
            else:
                pass

        tie_list.clear()

        valid_moves.clear()
        point = warns_move

        used_moves.add(warns_move)

        if (headless == True):
            pass
        else:
            from draw import draw_pattern
            draw_pattern(sample_surface, size, warns_move, grid_coordinates)




        



        

        



        
